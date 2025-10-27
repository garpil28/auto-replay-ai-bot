from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from ai_responses import get_random_response
from config import TOKEN
from database import init_db, add_user

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    add_user(user.id, user.username, user.first_name)
    response = get_random_response()
    await update.message.reply_text(response)

if __name__ == "__main__":
    print("🚀 Garfield Auto Reply Bot is running...")
    init_db()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))
    app.run_polling()
