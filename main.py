from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardRemove
import email
import numbers
import requests
import logging

token = '5725922607:AAEmeee4O3vA2ZCkQcjYgCFJqEJVoaQ_X2w'
logging.basicConfig(level=logging.INFO)

bot = Bot(token)
ab = Dispatcher(bot)

btnmain = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btnmain.add("Courses 📚", "About us 📔", "Contact and Location 📌")

btncourses = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btncourses.add("Backend", "Frontend", "Data science", "Python", "Android", "Menu 📤")

btnaccept = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btnaccept.add('Enroll 🖋', 'Back ⬅️', 'Menu 📤')

btnback = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btnback.add('Back ⬅️', 'Menu 📤')

inlinetg = types.InlineKeyboardButton("Telegram", url="telegram.com")
inlinein = types.InlineKeyboardButton("Instagram", url="instagram.com")
inlineyt = types.InlineKeyboardButton("Youtube", url="youtube.com")
inlinevd = types.InlineKeyboardButton("Video", callback_data="Video")
inline = types.InlineKeyboardMarkup().add(inlinetg, inlinein, inlineyt, inlinevd)


@ab.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Dear {message.chat.first_name}, you are welcome to Project!", reply_markup=btnmain)


@ab.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Describe your problem here 👇")


@ab.message_handler(text='Courses 📚')
async def courses(message: types.Message):
    await message.answer("Which one you will choose?", reply_markup=btncourses)


@ab.message_handler(text='About us 📔')
async def about(message: types.Message):
    rasm = open("pict/photo-1515378791036-0648a3ef77b2.jpg", "rb")
    word = "Project company\n\nIt's high qualified online bot where you can find different types of video courses and learn it." \
           "our company did their best to create a great opportunity and comfort for future students. Quality is always in" \
           "first place to company so that's why we pay attention to this. According to people's money we tried to set the" \
           "price of the courses, we did pay attention to poor people. That's neccessary to have permisson to everyone no" \
           "matter poor he is or not. Our company Project!"
    await bot.send_photo(message.chat.id, rasm, caption=word, reply_markup=inline)


@ab.callback_query_handler(text=['Video'])
async def video(message: types.CallbackQuery):
    video = open("pict/video.mp4", "rb")
    msg = "Here is the video where you can find more information about it from owner of the company"
    await bot.send_video(message.from_user.id, video, caption=msg)


@ab.message_handler(text='Contact and Location 📌')
async def locandcon(message: types.Message):
    await message.answer("Our location 👇")
    await bot.send_location(message.chat.id, "39.7681° N", "64.4556° E")
    await message.answer("Our number 👇")
    await bot.send_contact(message.chat.id, "+998909094955", "Project")


@ab.message_handler(text='Backend')
async def backend(message: types.Message):
    rasm1 = open("pict/backend.jpg", "rb")
    word1 = "Backend\n\nBack-end developers are the experts who build and maintain the mechanisms " \
            "that process data and perform actions on websites.That's cool because they know hot" \
            "code programms, telegram bots or even sites you know what it is\n\nPrice:300$"
    await bot.send_photo(message.chat.id, rasm1, caption=word1, reply_markup=btnaccept)


@ab.message_handler(text='Frontend')
async def backend(message: types.Message):
    rasm2 = open("pict/frontend.jpg", "rb")
    word2 = "Frontend\n\nA front-end developer creates websites and applications using web languages " \
            "such as HTML, CSS, and JavaScript that allow users to access and interact with the site " \
            "or app. When you visit a web or website, the design elements you see were created by a front-end developer" \
            "\n\nPrice:280$"
    await bot.send_photo(message.chat.id, rasm2, caption=word2, reply_markup=btnaccept)


@ab.message_handler(text='Data science')
async def backend(message: types.Message):
    rasm3 = open("pict/data.png", "rb")
    word3 = "Data science\n\nA data scientist is a professional responsible for collecting, analyzing and " \
            "interpreting extremely large amounts of data. The data scientist role is an offshoot of several " \
            "traditional technical roles, smth including mathematician, scientist, statistician and computer professional" \
            "\n\nPrice:700$"
    await bot.send_photo(message.chat.id, rasm3, caption=word3, reply_markup=btnaccept)


@ab.message_handler(text='Python')
async def backend(message: types.Message):
    rasm4 = open("pict/pytho.png", "rb")
    word4 = "Python\n\nPython developers design, code, and deploy development projects in the Python language. " \
            "They also work on debugging those same projects to ensure they function as intended. As a python " \
            "developer, you'll work closely with other teams, including data collection and analytics, to help " \
            "answer questions and provide insight\n\nPrice:340$"
    await bot.send_photo(message.chat.id, rasm4, caption=word4, reply_markup=btnaccept)


@ab.message_handler(text='Android')
async def backend(message: types.Message):
    rasm5 = open("pict/java.png", "rb")
    word5 = "Android\n\nAndroid developer is responsible for developing applications for devices powered by " \
            "the Android operating system. Due to the fragmentation of this ecosystem, an Android developer " \
            "must pay special attention to the application's compatibility with multiple versions of Android " \
            "and device types\n\nPrice:450$"
    await bot.send_photo(message.chat.id, rasm5, caption=word5, reply_markup=btnaccept)


@ab.message_handler(text='Enroll 🖋')
async def getsdfs(message: types.Message):
    await message.answer('Leave your email 👇', reply_markup=btnback)


@ab.message_handler(text='Back ⬅️')
async def back(message: types.Message):
    await message.answer('You came back to previous page', reply_markup=btncourses)


@ab.message_handler(text_contains=['@gmail.'])
async def numbers(message: types.Message):
    await message.answer('Your order was accepted, please check your email ✅', reply_markup=btnmain)


@ab.message_handler(text='Menu 📤')
async def menu(message: types.Message):
    await message.answer('You was successfully returned to main menu', reply_markup=btnmain)


if __name__ == '__main__':
    executor.start_polling(ab, skip_updates=True)
