import telebot
import os

# Бот токенді орта айнымалыдан аламыз (Render-де BOT_TOKEN деп қосамыз)
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# /start командасына жауап
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "👋 Сәлем! ClashMarket ботына қош келдің!\n\n"
        "📱 Мұнда Clash of Clans аккаунттарын сатып алуға болады.\n"
        "🛒 Сатылымдағы аккаунттар жақында қосылады!"
    )

# Басқа хабарламаларға жауап
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(
        message.chat.id,
        "⏳ Қазіргі уақытта тек /start командасы жұмыс істейді.\n"
        "📦 Толық функционал жақында қосылады!"
    )

# Бот үзіліссіз жұмыс істейді
bot.infinity_polling()
