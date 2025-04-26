

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Set up logging to help with debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Correctly assign your token here
TOKEN = '8093815852:AAEXPNO4g6nB7ifqdgoOzvffW0oz1NFOLsI'  # Replace this with your token

# Command handler functions

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hi! I am your bot.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here are the available commands: /start, /help, /image1, /doc1, etc.')

async def image1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here is image 1!')

async def image2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here is image 2!')

async def doc1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here is document 1!')

async def doc2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here is document 2!')

async def ayah(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here is an Ayah!')

async def dua(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here is a Dua!')

# Include the rest of your commands here:
# Example of how to add more commands like /image3, /doc3, etc.
async def image3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here is image 3!')

async def image4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here is image 4!')

async def doc3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here is document 3!')

async def doc4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here is document 4!')

# Add other commands as per your requirements

# Main function to set up the bot and handle the commands
async def main() -> None:
    # Set up the application with your token
    application = Application.builder().token(TOKEN).build()

    # Add command handlers for each of the commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("image1", image1))
    application.add_handler(CommandHandler("image2", image2))
    application.add_handler(CommandHandler("doc1", doc1))
    application.add_handler(CommandHandler("doc2", doc2))
    application.add_handler(CommandHandler("ayah", ayah))
    application.add_handler(CommandHandler("dua", dua))
    application.add_handler(CommandHandler("image3", image3))
    application.add_handler(CommandHandler("image4", image4))
    application.add_handler(CommandHandler("doc3", doc3))
    application.add_handler(CommandHandler("doc4", doc4))
    # Add more handlers for your other commands here

    # Start the bot
    await application.run_polling()

# Run the main function
if __name__ == "__main__":
    import asyncio
if __name__ == "__main__":
    from telegram.ext import Application
    application = Application.builder().token(TOKEN).build()
    application.run_polling()
