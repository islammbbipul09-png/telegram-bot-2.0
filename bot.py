import os
import telebot

# Telegram Bot Token পরিবেশ ভ্যারিয়েবল থেকে আনবে
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

# Start কমান্ড
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Bot is running 24/7 on Railway!")

# টেক্সট মেসেজ হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"আপনি লিখেছেন: {message.text}")

print("🤖 Bot is running...")
bot.infinity_polling()
