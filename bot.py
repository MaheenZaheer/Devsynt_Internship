import requests
import discord

intents = discord.Intents.default()
intents.message_content = True  # Already enabled in Developer Portal

client = discord.Client(intents=intents)

# Your ngrok webhook URL from n8n
N8N_WEBHOOK_URL = (
    "https://jab-fame-trimester.ngrok-free.dev/webhook-test/webhook"
)


@client.event
async def on_message(message):
  # Ignore messages sent by the bot itself or Captain Hook
  if message.author.bot:
    return

  # Send incoming message to n8n
  payload = {
      "user": str(message.author),
      "content": message.content,
      "channel_id": str(message.channel.id),
  }
  requests.post(N8N_WEBHOOK_URL, json=payload)


client.run("YOUR_DISCORD_BOT_TOKEN_HERE")
