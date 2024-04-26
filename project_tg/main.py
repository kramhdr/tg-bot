import logging
from telegram.ext import Application, MessageHandler, filters
from config import BOT_TOKEN
from telegram.ext import CommandHandler
from random import randint
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
reply_keyboard = [['/4', '/7'],
                  ['/8', '/14']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def site(update, context):
    await update.message.reply_text(
        """Сайт с полезной информацией для подготовки к ЕГЭ: 
https://kompege.ru/""")


async def open_python(update, context):
    await update.message.reply_text(
        """Онлайн версия языка питон: 
https://www.online-python.com/""")


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


async def help(update, context):
    await update.message.reply_text(
        """Я бот-помощник для подготовки к ЕГЭ по информатике.
После того как вы кликните на нужный номер, я пришлю вам вопрос.
После этого вы должны написать ваш ответ и отправить.
Не используйте пробелы и единицы измерения.
Когда вы отправите свой ответ, я сообщу вам результат.
Чтобы научиться решать какой-либо тип номеров или усовершенствовать свои навыки, вы можете перейти на сайт с полезными ресурсами /site
Если вам мешает клавиатура, вы можете отключить её по команде /close
В таком случае вам придется выбирать задание с помощью команд, то есть через / и номер необходимого задания.
 Если вы не можете воспользоваться компьютером, а для решения задания необходим язык программирования, воспользуйтесь командой /python чтобы открыть онлайн версию языка питон.""")


def choose_number():
    return randint(1, 5)


def open7():
    number = choose_number()
    f = open(f'data/7/{number}.txt', 'r', encoding="utf-8").readlines()
    text = f[0]
    ans = f[1]

    return text, ans


async def n_7_question(update, context):
    text, ans = open7()
    context.user_data['locality'] = ans
    await update.message.reply_text(
        str(text))


async def n_7_answer(update, context):
    cur_ans = context.user_data['locality']
    a = update.message.text
    if a == cur_ans:
        await update.message.reply_text(
            'Верно')
    else:
        await update.message.reply_text(
            f'Неверно Правильный ответ - {cur_ans}')
    context.user_data.clear()


def open4():
    number = choose_number()
    f = open(f'data/4/{number}.txt', 'r', encoding="utf-8").readlines()
    text = f[0]
    ans = f[1]

    return text, ans


async def n_4_question(update, context):
    text, ans = open4()
    context.user_data['locality'] = ans
    await update.message.reply_text(
        str(text))


async def n_4_answer(update, context):
    cur_ans = context.user_data['locality']
    a = update.message.text
    if a == cur_ans:
        await update.message.reply_text(
            'Верно')
    else:
        await update.message.reply_text(
            f'Неверно Правильный ответ - {cur_ans}')
    context.user_data.clear()


def open8():
    number = choose_number()
    f = open(f'data/8/{number}.txt', 'r', encoding="utf-8").readlines()
    text = f[0]
    ans = f[1]

    return text, ans


async def n_8_question(update, context):
    text, ans = open8()
    context.user_data['locality'] = ans
    await update.message.reply_text(
        str(text))


async def n_8_answer(update, context):
    cur_ans = context.user_data['locality']
    a = update.message.text
    if a == cur_ans:
        await update.message.reply_text(
            'Верно')
    else:
        await update.message.reply_text(
            f'Неверно Правильный ответ - {cur_ans}')
    context.user_data.clear()


def open14():
    number = choose_number()
    f = open(f'data/14/{number}.txt', 'r', encoding="utf-8").readlines()
    text = f[0]
    ans = f[1]

    return text, ans


async def n_14_question(update, context):
    text, ans = open14()
    context.user_data['locality'] = ans
    await update.message.reply_text(
        str(text))


async def n_14_answer(update, context):
    cur_ans = context.user_data['locality']
    a = update.message.text
    if a == cur_ans:
        await update.message.reply_text(
            'Верно')
    else:
        await update.message.reply_text(
            f'Неверно Правильный ответ - {cur_ans}')
    context.user_data.clear()


async def start(update, context):
    await update.message.reply_text(
        """    Здравствуйте! Я бот, помогающий подготовиться к ЕГЭ по информатике.
Вы можете выбрать интересующий вас номер с клавиатуры.
Чтобы подробнее узнать о функциях бота, вы можете написать /help""",
        reply_markup=markup
    )


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("7", n_7_question))
    application.add_handler(CommandHandler("4", n_4_question))
    application.add_handler(CommandHandler("8", n_8_question))
    application.add_handler(CommandHandler("14", n_14_question))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("site", site))
    application.add_handler(CommandHandler("python", open_python))
    text_handler = MessageHandler(filters.TEXT, n_7_answer)
    text_handler = MessageHandler(filters.TEXT, n_4_answer)
    text_handler = MessageHandler(filters.TEXT, n_8_answer)
    text_handler = MessageHandler(filters.TEXT, n_14_answer)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
