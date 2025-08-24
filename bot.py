import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

AGENCY = "Crypto Listing Hub"
ADMIN = os.getenv("ADMIN_USERNAME", "youradmin")
GROUP = os.getenv("TELEGRAM_GROUP", "")

WELCOME = f"""🚀 Welcome to {AGENCY}!

We help crypto projects with:
• ✅ Tier-1 & Tier-2 Exchange Listings
• ✅ CoinMarketCap & CoinGecko Listings
• ✅ Marketing & Trending Campaigns
• ✅ MM Bots & Liquidity
• ✅ Automation Bots & DB Outreach

👤 Contact: @{ADMIN}
{('📣 Group: ' + GROUP) if GROUP else ''}
Type *services* anytime to see full services.
"""

SERVICES = f"""📋 Services — {AGENCY}
• Exchange Listings: Tier-1 & Tier-2
• CMC/CG Listings & Data setup
• Marketing, KOLs, AMAs, Trending
• MM Bots, Liquidity & Growth
👤 Admin: @{ADMIN}
"""

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME, disable_web_page_preview=True)

async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").lower()
    if "services" in text:
        await update.message.reply_text(SERVICES, disable_web_page_preview=True)
    else:
        await update.message.reply_text(WELCOME, disable_web_page_preview=True)

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise SystemExit("BOT_TOKEN missing")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.run_polling()

if __name__ == "__main__":
    main()
