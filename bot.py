from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import random

# Опции для игры
choices = ["камень", "ножницы", "бумага"]

async def start(update: Update, context):
    await update.message.reply_text("Привет! Напиши 'камень', 'ножницы' или 'бумага' для игры.")

async def play(update: Update, context):
    user_choice = update.message.text.lower()
    bot_choice = random.choice(choices)
    if user_choice not in choices:
        await update.message.reply_text("Выберите только: 'камень', 'ножницы' или 'бумага'.")
    else:
        result = determine_winner(user_choice, bot_choice)
        await update.message.reply_text(f"Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}\n{result}")

def determine_winner(user, bot):
    if user == bot:
        return "Ничья!"
    elif (user == "камень" and bot == "ножницы") or \
         (user == "ножницы" and bot == "бумага") or \
         (user == "бумага" and bot == "камень"):
        return "Вы выиграли!"
    else:
        return "Вы проиграли!"

TOKEN = "8144707764:AAGSW2LIeHdswTEhH9LluWdQOhtIxh7jxdc"
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, play))

print("Бот запущен. Нажмите Ctrl+C для остановки.")
app.run_polling()
