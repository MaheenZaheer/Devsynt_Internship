SlotWise — AI Booking Concierge Bot
SlotWise is an automated AI booking assistant that manages customer appointment reservations directly in Discord. Built using n8n, Google Gemini 1.5 Flash, and Google Sheets, it checks live spreadsheet data before responding to eliminate AI hallucinations and ensure offered time slots are accurate.

How It Works
A user posts a message in the Discord channel.

A background Python script listens to the message and forwards it to an n8n webhook via an ngrok tunnel.

n8n fetches all rows from a Google Sheet where the status is marked as available.

A JavaScript code step merges the returned rows into a single list so downstream steps only run once.

Google Gemini receives the user's message alongside the real available time slots and drafts a single concise reply.

n8n logs the user's name, message, and AI reply into an audit log sheet.

n8n sends the finalized message back to the Discord channel using a Discord Webhook.

Features
Ground-Truth Data Verification: Ensures the bot only offers time slots that are currently marked available in your database.

Duplicate Prevention: Consolidates database rows into a single execution stream so the bot never sends repeating messages.

Bi-Directional Messaging: Receives user queries from Discord and posts responses back automatically.

Transaction Logging: Keeps a complete history of user inquiries and bot responses in Google Sheets.

System Requirements
Node.js and n8n running locally.

Python 3.10 or higher.

ngrok CLI for tunneling.

A Google Cloud Console project with Google Sheets and Google Drive APIs enabled.

A Discord Developer Application with Message Content Intent enabled.