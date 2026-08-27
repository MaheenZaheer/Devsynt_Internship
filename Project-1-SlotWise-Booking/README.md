<div align="center">

# 🤖 SlotWise — AI Booking Concierge Bot

**An intelligent Discord appointment booking assistant powered by AI and real-time database validation.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![n8n](https://img.shields.io/badge/n8n-Workflow-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini_1.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Google Sheets](https://img.shields.io/badge/Google-Sheets-34A853?style=for-the-badge&logo=googlesheets&logoColor=white)](https://workspace.google.com/products/sheets/)
[![Discord](https://img.shields.io/badge/Discord-Bot-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/)

</div>

---

## 📖 Overview

**SlotWise** is an AI-powered booking concierge that automates appointment scheduling directly inside **Discord**.

Unlike traditional chatbots that may hallucinate available appointments, SlotWise verifies every response against a live **Google Sheets** database before generating a reply. Using **Google Gemini 1.5 Flash** within an **n8n** workflow, it ensures users only receive **accurate, real-time availability**.

Every interaction is also logged for auditing, making the system reliable for businesses handling appointment bookings.

---

## ✨ Features

- ✅ **Live Slot Verification**
  - Reads available appointment slots directly from Google Sheets before responding.

- 🤖 **AI-Powered Conversations**
  - Uses Google Gemini 1.5 Flash to generate natural and context-aware responses.

- 🚫 **No Hallucinated Availability**
  - AI is grounded using live database records.

- 🔄 **Duplicate Response Prevention**
  - Consolidates spreadsheet rows into a single execution to avoid repeated replies.

- 💬 **Real-Time Discord Integration**
  - Automatically receives customer messages and replies instantly.

- 📝 **Audit Logging**
  - Stores every user query and AI response inside Google Sheets.

- ⚡ **Fully Automated Workflow**
  - Built with n8n for low-code automation.

---

# 🏗️ System Architecture

```
Discord User
      │
      ▼
Python Listener (bot.py)
      │
      ▼
ngrok Tunnel
      │
      ▼
n8n Webhook
      │
      ▼
Google Sheets
(Check Available Slots)
      │
      ▼
JavaScript Merge Node
      │
      ▼
Google Gemini 1.5 Flash
      │
      ▼
Google Sheets
(Audit Log)
      │
      ▼
Discord Webhook
      │
      ▼
Customer Receives Response
```

---

# ⚙️ Workflow

### 1️⃣ Customer Sends a Message

A user requests an appointment in the designated Discord booking channel.

---

### 2️⃣ Python Listener

A background Python application listens for Discord messages and forwards them to an **n8n webhook** using **ngrok**.

---

### 3️⃣ Live Database Lookup

The n8n workflow queries Google Sheets to retrieve every row marked:

```
available
```

---

### 4️⃣ Merge Available Slots

A custom JavaScript node merges multiple spreadsheet rows into one array, ensuring only **one downstream execution**.

---

### 5️⃣ AI Response Generation

Google Gemini 1.5 Flash receives:

- Customer message
- Available time slots

It then generates a natural response strictly based on those slots.

---

### 6️⃣ Audit Logging

The workflow records:

- Username
- Customer query
- AI response

inside an audit Google Sheet.

---

### 7️⃣ Discord Reply

The generated response is automatically posted back to Discord using a webhook.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Discord Listener |
| Discord.py | Discord Integration |
| n8n | Workflow Automation |
| Google Gemini 1.5 Flash | AI Response Generation |
| Google Sheets | Appointment Database |
| Google Sheets API | Data Access |
| JavaScript | Data Consolidation |
| ngrok | Local Webhook Tunnel |

---

# 📂 Project Structure

```
SlotWise/
│
├── bot.py
├── requirements.txt
├── My workflow 2 (2).json
├── README.md
└── assets/
```

---

# 📋 Prerequisites

Before running the project, ensure you have:

- Python **3.10+**
- Node.js
- n8n
- ngrok CLI
- Google Cloud Project
- Google Sheets API enabled
- Google Drive API enabled
- Google Gemini API Key
- Discord Bot Token
- Discord Message Content Intent enabled

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/MaheenZaheer/Devsynt_Internship.git

cd Devsynt_Internship
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Start n8n

```bash
n8n start
```

---

## 4. Expose Localhost using ngrok

```bash
ngrok http 5678
```

Copy the generated HTTPS URL and configure it wherever required.

---

## 5. Import the Workflow

Open

```
http://localhost:5678
```

Then:

- Import `My workflow 2 (2).json`
- Configure Google Sheets credentials
- Configure Google Gemini credentials
- Activate the workflow

---

## 6. Run the Discord Bot

```bash
python bot.py
```

---

# 🔑 Required Credentials

You'll need:

- Discord Bot Token
- Discord Webhook URL
- Google Gemini API Key
- Google OAuth Credentials
- Google Sheets Access

---

# 📊 Example Conversation

**User**

```
I want an appointment tomorrow afternoon.
```

**Bot**

```
The following slots are currently available tomorrow:

• 2:00 PM
• 3:30 PM
• 5:00 PM

Please let me know which one you'd like to reserve.
```

---

# 📈 Future Improvements

- Calendar integration
- Automatic slot reservation
- Multi-business support
- Email confirmations
- WhatsApp integration
- Admin dashboard
- Booking cancellation
- Customer authentication

---

# 👩‍💻 Author

**Maheen Zaheer**

Computer Engineering Student  
University of Engineering and Technology (UET) Lahore

GitHub:
> https://github.com/MaheenZaheer

---

# 📄 License

This project is intended for educational and internship purposes.
