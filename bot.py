import telebot

# BotFather ဆီက ရထားတဲ့ ကိုယ့်ရဲ့ Bot Token ကို အောက်ပါ ကွင်းစကွင်းပိတ်ထဲမှာ ထည့်ပါ
TOKEN = '8947621195:AAGRZBV5Iyotz5yuPkTOdosda9XmLvIokxM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါ! Wi-Fi ဘောင်ချာကုဒ်ထုတ်ရန် /voucher ဟု ရိုက်နှိပ်ပါ။")

@bot.message_handler(commands=['voucher'])
def generate_voucher(message):
    # ဤနေရာတွင် ဘောင်ချာကုဒ် ထုတ်ပေးမည့် ကုဒ်များကို ထည့်သွင်းရပါမည်
    voucher_code = "WIFI-1234-5678" 
    bot.reply_to(message, f"သင့်ရဲ့ Wi-Fi ဘောင်ချာကုဒ် - `{voucher_code}`")

bot.polling()
