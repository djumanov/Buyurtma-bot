from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text(text='Hello! 👋 \nThis is a demo version of the Telegram Store bot. You can test out catalog function and checkout process.')

    