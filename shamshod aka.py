from aiogram import Bot, Dispatcher, executor, types
import requests
import logging

token = '5669477242:AAG07y5yMsBNjT2Me5fb3QoA_W0dm6IyB3w'
logging.basicConfig(level=logging.INFO)

bot = Bot(token)
hey = Dispatcher(bot)


answers = [
    'yes',
    'no'
]

btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn.add('play', 'dont play')

savol1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
savol1.add('yes', 'no', 'maybe')

savol2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
savol2.add('yes', 'no', 'maybe')


@hey.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.reply('Welcome', reply_markup=btn)


@hey.message_handler(text=['play'])
async def play(message: types.Message):
    await message.answer('birinchi savol', reply_markup=savol1)


@hey.message_handler(content_types="text")
async def playyy(message: types.Message):
    s = 0
    msg = message.text
    if msg in answers:
        s += 1
        await message.answer('kengi savol', reply_markup=savol2)
    else:
        await message.answer('kengi savol', reply_markup=savol2)


if __name__ == '__main__':
    executor.start_polling(hey,skip_updates=True)
