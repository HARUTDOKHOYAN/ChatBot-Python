import telebot
import BooksRepo
from telebot import types
from config import TOKEN , STARTFOLDER


bot = telebot.TeleBot(TOKEN)
books = BooksRepo.Repository()
books.InitDirectory()


@bot.message_handler(commands=["start"])
def start(message):
    BooksRepo.CurrentFolder = "testDr"
    mess = f"Hi <b>{message.from_user.first_name}</b>  It is Books Repository"
    markup = books.CreatFolderMarkups(STARTFOLDER)
    bot.send_message(message.chat.id, mess,
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(func=lambda messag: books.IsConteinFolder(messag.text))
def FolderHansler(message):
    BooksRepo.CurrentFolder = message.text
    markup = books.CreatFolderMarkups(message.text)
    mess = f"Choose folder or write name of preferable file \n {books.GetFilesList(message.text)}"
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(func=lambda messag: messag.text == "<--Back")
def FolderBeckHansler(message):
    parentFolder = books.FindParentFolder(BooksRepo.CurrentFolder)
    if (parentFolder == None):
        return
    BooksRepo.CurrentFolder = parentFolder.Name
    markup = books.CreatFolderMarkups(parentFolder.Name)
    mess = f"Choose folder or write name of preferable file \n {books.GetFilesList(parentFolder.Name)}"
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def GetFile(message):
    filePath = books.GetFileFromFolder(BooksRepo.CurrentFolder, message.text)
    if filePath != None:
        doc = open(filePath, 'rb')
        bot.send_document(message.chat.id, doc)
    else:
        mess = f"Not Found File \n Choose folder or write name of preferable file \n {books.GetFilesList(BooksRepo.CurrentFolder)}"
        bot.send_message(message.chat.id, mess)


# @bot.message_handler(commands=["dock"])
# def start(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton(
#         "Click", callback_data="good"))
#     mess = f"Hi <b>{message.from_user.first_name }</b>"
#     bot.send_message(message.chat.id, mess,
#                      parse_mode='html', reply_markup=markup)


# @bot.message_handler(commands=["help"])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     websyte = types.KeyboardButton("Dock")
#     hi = types.KeyboardButton("Hi")

#     markup.add(websyte, hi)
#     mess = f"Hi <b>{message.from_user.first_name }</b>"
#     bot.send_message(message.chat.id, mess,
#                      parse_mode='html', reply_markup=markup)


# @bot.message_handler(func=lambda message: message.text == "harut")
# def get_user_text(message):
#     bot.send_message(message.chat.id, message, parse_mode='html')


# @bot.callback_query_handler(func=lambda call: True)
# def test_callback(call):  # <- passes a CallbackQuery type object to your function
#     try:
#         bot.send_message(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                          text=f"{call.message.chat}", parse_mode="html")
#     except Exception as e:
#         print(e)


bot.polling(non_stop=True)
