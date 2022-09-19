from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from commands import start
from services import administration, administration_exit


def main() -> None:
    """Start the bot."""
    TOKEN = os.environ['TOKEN']
    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(handler=CommandHandler(command=['start', 'boshlash'], callback=start))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('🎛 Administration'), callback=administration))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('🚪 Exit'), callback=administration_exit))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()