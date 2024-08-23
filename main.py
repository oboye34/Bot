from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from PIL import Image

# توكين البوت
TOKEN = '7530009252:AAH1ky8eV0cgsmCNAepfGJx775uAa4eCS9g'

# حجم الشعار
LOGO_SIZE = (250, 250)

# تحميل الشعار
logo = Image.open('your_logo.png').convert("RGBA")
logo.thumbnail(LOGO_SIZE)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحباً! أرسل لي صورة وسأضيف عليها الشعار.')

def handle_photos(update: Update, context: CallbackContext) -> None:
    photo = update.message.photo[-1]  # استخدم أكبر دقة للصورة المستلمة
    file = photo.get_file()
    file.download('received_image.jpg')

    with Image.open('received_image.jpg') as img:
        img.paste(logo, (20, 20), logo)
        img.save('output_image.jpg')

    with open('output_image.jpg', 'rb') as file:
        update.message.reply_photo(photo=InputFile(file))

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_photos))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()