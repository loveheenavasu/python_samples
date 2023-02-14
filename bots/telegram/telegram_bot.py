import telegram.ext


def start(update, context):
    update.message.reply_text("Hello! Welcome to Zestgeek Sloutions")


def help(update, context):
    update.message.reply_text("""
    The following commands are avilable:

    /start -> Welcome to the channel
    /help -> This message
    /content -> Simplilearn offers various courses free of course through Skillup by Simplilearn
    /Python  -> The first video from Python Playlist
    /SQL -> The first video from SQL Playlist
    /Java -> The first video from Java Playlist
    /Skillup -> Free platform for certification by Simplilearn
    /contact -> contact information 
     """)


def content(update, context):
    update.message.reply_text("We have various songs playlists")


def Hindi(update, context):
    update.message.reply_text("tutorial link : https://www.youtube.com/watch?v=wDm7PtFXUQo")


def Punjabi(update, context):
    update.message.reply_text("tutorial link : https://www.youtube.com/watch?v=tpFljbJxZiw")


def Phadi(update, context):
    update.message.reply_text("tutorial link : https://www.youtube.com/watch?v=V0tLmW9T1pc")


def Arabic(update, context):
    update.message.reply_text(
        "tutorial link : https://www.youtube.com/watch?v=GuGYYdwcPYw")


def contact(update, context):
    update.message.reply_text("You can contact on the official mail id")


def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")


Token = ("6269557659:AAEVBiPrBpXgOZr0PEVwtU2W7BsVPHxqFzo")
# print(bot.get_me())
updater = telegram.ext.Updater("6269557659:AAEVBiPrBpXgOZr0PEVwtU2W7BsVPHxqFzo", use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('help', help))
disp.add_handler(telegram.ext.CommandHandler('content', content))
disp.add_handler(telegram.ext.CommandHandler('Hindi', Hindi))
disp.add_handler(telegram.ext.CommandHandler('Punjabi', Punjabi))
disp.add_handler(telegram.ext.CommandHandler('Phadi', Phadi))
disp.add_handler(telegram.ext.CommandHandler('Arabic', Arabic))
disp.add_handler(telegram.ext.CommandHandler('contact', contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()