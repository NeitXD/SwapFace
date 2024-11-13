# NeitXD
# main.py
from dotenv import load_dotenv
import os

load_dotenv()  # Add this to load .env variables

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from database import add_user, get_user, update_credits, extract_db
from faceswap_image import swap_face_image
from faceswap_video import swap_face_video
import configs

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    credits = user['credits'] if user else 0
    await update.message.reply_text(
        f"Welcome! Your ID is {user_id}. You have {credits} credits."
    )
    add_user(user_id, credits)
    if credits <= configs.LOW_CREDIT_THRESHOLD:
        await update.message.reply_text("Warning: Your credits are low!")

async def refill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != configs.ADMIN_ID:
        await update.message.reply_text("Only the admin can add credits.")
        return
    try:
        user_id = int(context.args[0])
        amount = int(context.args[1])
        update_credits(user_id, amount)
        await update.message.reply_text(f"Added {amount} credits to user {user_id}.")
    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /refill <user_id> <amount>")
    except Exception as e:
        logging.error(f"Error refilling credits: {e}")

async def db_extract(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != configs.ADMIN_ID:
        await update.message.reply_text("Unauthorized.")
        return
    data = extract_db()
    await update.message.reply_text(f"Database: {data}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start bot\n"
        "/refill <user_id> <amount> - Add credits to a user (admin only)\n"
        "/db_extract - Extract the user database (admin only)\n"
        "/help - Show available commands\n"
    )

if __name__ == "__main__":
    application = ApplicationBuilder().token(configs.BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("refill", refill))
    application.add_handler(CommandHandler("db_extract", db_extract))
    application.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    application.run_polling()
