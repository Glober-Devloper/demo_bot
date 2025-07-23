# ✅ Telegram Bot for Render Deployment

This bot includes:
- /start and /help commands
- Echo message handler
- Uses environment variable for token
- Ready for 24/7 hosting on Render

---

## 🔧 Setup Instructions

1. Push this folder to a GitHub repo
2. Go to https://render.com → New Web Service → Connect your repo
3. Make sure your `render.yaml` and `start.sh` are in the repo root
4. In Render dashboard:
   - Set Environment Variable:
     - `BOT_TOKEN = <your_telegram_bot_token>`
   - Make sure start command is: `bash start.sh`
5. Click Deploy

Your bot will be live 24/7 🚀
