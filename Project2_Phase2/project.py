import os
from typing import TypedDict, Optional
import pandas as pd
import matplotlib.pyplot as plt
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END


# 1. DEFINE SHARED STATE
class PipelineState(TypedDict):
    csv_path: str
    cleaned_df: Optional[pd.DataFrame]
    summary_text: Optional[str]


# 2. DEFINE AGENT NODES
def clean_data_node(state: PipelineState) -> dict:
    """Node 1: Reads raw CSV file and drops null/duplicate values."""
    print("\n--- [1/3] Cleaning Data ---")
    
    csv_path = state["csv_path"]
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Source data file '{csv_path}' not found at: {csv_path}")
        
    df = pd.read_csv(csv_path, encoding='latin1')
    
    # Cleaning operations
    df = df.drop_duplicates()
    df = df.fillna(0)
    
    return {"cleaned_df": df}


def analyze_data_node(state: PipelineState) -> dict:
    """Node 2: Extracts basic dataset info and gets a summary from Groq."""
    print("--- [2/3] Analyzing Data with Groq ---")
    df = state["cleaned_df"]
    
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is missing! Please set it before running.")

    # Using active model endpoint from your account's model list
    model_instance = ChatGroq(
        model="qwen/qwen3.6-27b",
        api_key=api_key
    )
    
    prompt = f"Write a short 2-sentence summary of a dataset containing {len(df)} rows and {len(df.columns)} columns."
    
    response = model_instance.invoke(prompt)
    
    print("\n[Groq Executive Summary]:")
    print(response.content)
    
    return {"summary_text": response.content}


def visualize_data_node(state: PipelineState) -> dict:
    """Node 3: Plot key metrics on independent subplots without scale distortion."""
    print("\n--- [3/3] Displaying Visualizations ---")
    df = state["cleaned_df"]
    
    # Create a figure with 3 separate subplots side-by-side
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    
    # Subplot 1: Total Revenue (Single Bar)
    if 'sales_amount' in df.columns:
        total_sales = df['sales_amount'].sum()
        axes[0].bar(['Total Sales'], [total_sales], color='skyblue', edgecolor='black')
        axes[0].set_title('Total Revenue ($)')
        axes[0].set_ylabel('Amount ($)')
        
    # Subplot 2: Unit Price Distribution (Histogram)
    if 'unit_price' in df.columns:
        axes[1].hist(df['unit_price'], bins=15, color='salmon', edgecolor='black')
        axes[1].set_title('Price Distribution')
        axes[1].set_xlabel('Price ($)')
        axes[1].set_ylabel('Frequency')
        
    # Subplot 3: Item Quantities (Categorical Bar Chart)
    if 'quantity' in df.columns:
        df['quantity'].value_counts().sort_index().plot(
            kind='bar', ax=axes[2], color='lightgreen', edgecolor='black'
        )
        axes[2].set_title('Item Quantity Counts')
        axes[2].set_xlabel('Quantity Units')
        axes[2].set_ylabel('Order Count')
        axes[2].tick_params(axis='x', rotation=0)

    plt.tight_layout()
    
    print("Opening plot window...")
    plt.show()
    return {}


# 3. BUILD AND WIRE THE GRAPH
builder = StateGraph(PipelineState)

builder.add_node("cleaner", clean_data_node)
builder.add_node("analyzer", analyze_data_node)
builder.add_node("visualizer", visualize_data_node)

builder.add_edge(START, "cleaner")
builder.add_edge("cleaner", "analyzer")
builder.add_edge("analyzer", "visualizer")
builder.add_edge("visualizer", END)

app = builder.compile()


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    YOUR_DATASET_PATH = os.path.join(base_dir, "retail_sales_dataset.csv")
    
    if not os.path.exists(YOUR_DATASET_PATH):
        parent_dir = os.path.dirname(base_dir)
        YOUR_DATASET_PATH = os.path.join(parent_dir, "retail_sales_dataset.csv")

    print(f"Starting pipeline on real dataset: {YOUR_DATASET_PATH}")
    app.invoke({"csv_path": YOUR_DATASET_PATH})