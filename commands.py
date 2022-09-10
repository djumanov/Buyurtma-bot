from telegram import ReplyKeyboardMarkup, Update, KeyboardButton
from telegram.ext import CallbackContext



def keyboard() -> list:
    """create welocome buttons."""
    keyboard = [
        [KeyboardButton(text='🏬 Catalog'), KeyboardButton(text='📦 Orders')],
        [KeyboardButton(text='👤 Userinfo'), KeyboardButton(text='🛒 Cart')],
        [KeyboardButton(text='🎛 Administration')],
    ]
    return keyboard



def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    text = 'Hello! 👋 \nThis is a demo version of the Telegram Store bot. You can test out catalog function and checkout process.'
    update.message.reply_text(text=text, reply_markup=ReplyKeyboardMarkup(keyboard=keyboard(), resize_keyboard=True))

