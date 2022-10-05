import json
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
import model_rac as m
lst = []

INP1, INP2, OPS = range(3)
print('Server started')

def log(update, context):
    file = open('log.json', 'a', encoding='utf-8')
    json.dump(f'{update.message.date} : {update.effective_user.first_name} - {update.message.text}   ', file, ensure_ascii=False)
    file.close()
    

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(        
        "Говорящий калькулятор, операции с дробями"
        "\nВведите первое число в виде дроби типа 3/8")
    log(update, context)
    return INP1


async def get_num1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    str1 = update.message.text
    lst.append(str1)
    answ = 'Не лучший выбор ' + str1 + ', ну да ладно\nЧешите следующее писло аналогично'
    await update.message.reply_text(answ)
    log(update, context)
    return INP2

async def get_num2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    str2 = update.message.text
    lst.append(str2)
    answ = 'Снова здорово ' + str2 + ', ну тут видимо ничего не поделать\nВыберите действие:   +   -   *  или  /'
    await update.message.reply_text(answ)
    log(update, context)
    return OPS



async def opers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    file = open('log.json', 'a')
    json.dumps(f'{update.effective_user.first_name},{update.message.text} ')
    file.close()
    c = update.message.text
    if c == '+':
        rez = m.summ(lst)
    if c == '-':
        rez = m.subtr(lst)
    if c == '*':
        rez = m.mult(lst)
    if c == '/':
        rez = m.div(lst)
    await update.message.reply_text(rez)
    log(update, context)
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(        
        "Ну, до следующего раза!")
    log(update, context)
    return ConversationHandler.END



def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5516351397:AAEGHZDdpR4gi-p1eUxfZjwxO8KV6ScenOg").build()

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)], 
        states={
            INP1: [MessageHandler(filters.TEXT, get_num1)],
            INP2: [MessageHandler(filters.TEXT, get_num2)],
            OPS: [MessageHandler(filters.TEXT, opers)],
                },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()
main()
