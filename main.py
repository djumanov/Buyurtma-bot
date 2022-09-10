from telegram.ext import Updater
import os


def main() -> None:
    """Start the bot."""
    TOKEN = os.environ['TOKEN']
    updater = Updater(token=TOKEN)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()