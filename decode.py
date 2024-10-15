from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import base64

# Define your decode function
def decode(update, context):
    try:
        # Get the message sent by the user
        encoded_string = update.message.text

        # Decode from base64
        decoded_string = base64.b64decode(encoded_string).decode('utf-8')

        # Send the decoded result back to the user
        update.message.reply_text(f"Decoded: {decoded_string}")
    except Exception as e:
        update.message.reply_text(f"Error decoding message: {str(e)}")

# Define the start function
def start(update, context):
    update.message.reply_text("Hi! Send me a base64 encoded string, and I'll decode it for you.")

# Main function to set up the bot
def main():
    # Replace 'YOUR TOKEN HERE' with your actual bot token from BotFather
    TOKEN = '7779037777:AAHNp_iyGyFlO2Ayi6jM_cbGaywyP4YIWec'

    # Create the Updater and pass your bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Add a message handler to decode incoming messages
    dp.add_handler(MessageHandler(Filters.text, decode))

    # Start the bot
    updater.start_polling()

    # Run the bot until Ctrl-C is pressed
    updater.idle()

if name == 'main':
    main()
