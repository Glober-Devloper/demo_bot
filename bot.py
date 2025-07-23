import os
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext
)
import keep_alive  # Flask keep-alive module

BOT_TOKEN = os.environ['BOT_TOKEN']

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('🚀 Bot is online!')

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)

def main():
    keep_alive.keep_alive()  # Start Flask thread

    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("🤖 Bot polling started...")
    app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
