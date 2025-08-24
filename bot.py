import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("👋 Welcome! I am your auto-reply bot.")

async def reply(update, context):
    await update.message.reply_text("✅ Thanks for your message, we'll get back to you!")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    app.run_polling()

if __name__ == "__main__":
    main()
