import telebot
from telebot import types

TOKEN = "8998509191:AAGgUtEk01-_pWvrzarSKdyU2tvWgbXTMIA"
bot = telebot.TeleBot(TOKEN)
ADMIN_ID = 5980583942

# Текст, який продає сам себе
MARKETING_TEXT = (
    "🎯 **TargetData: Екосистема прискореного зростання продажів**\n\n"
    "Ви залежите від випадкового трафіку? Ми пропонуємо інструмент для формування **передбачуваного доходу**. "
    "TargetData усуває розрив між вашим продуктом і клієнтом, готовим до покупки прямо зараз.\n\n"
    "📊 **Наші ключові рішення:**\n"
    "1️⃣ **Прецизійна лідогенерація:** Формуємо бази на основі вашої географії та інтересів аудиторії.\n"
    "2️⃣ **Інтелектуальна автоматизація:** Впроваджуємо Telegram-агентів, які продають 24/7 без вихідних.\n\n"
    "Оберіть напрямок, щоб почати трансформацію вашого бізнесу:"
)

def get_main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🎯 Замовити базу клієнтів", callback_data="db_info"),
        types.InlineKeyboardButton("🤖 Розробка Чат-бота", callback_data="bot_info"),
        types.InlineKeyboardButton("💰 Прайс та Кейси", callback_data="price"),
        types.InlineKeyboardButton("💬 Зв'язатися з експертом", callback_data="support")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, MARKETING_TEXT, reply_markup=get_main_menu(), parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    if call.data == "db_info":
        bot.send_message(chat_id, "🎯 **Бази клієнтів:** Напишіть вашу нішу та місто, щоб ми підготували вибірку.")
    elif call.data == "bot_info":
        bot.send_message(chat_id, "🤖 **Автоматизація:** Опишіть ваш продукт, і ми прорахуємо архітектуру бота.")
    elif call.data == "price":
        bot.send_message(chat_id, "💰 **Прайс:**\n- База від 2000 грн\n- Чат-боти від 5000 грн\nПишіть в підтримку для прорахунку.")
    elif call.data == "support":
        bot.send_message(chat_id, f"👨‍💻 Експерт на зв'язку: tg://user?id={ADMIN_ID}")

if __name__ == "__main__":
    bot.polling(none_stop=True)
