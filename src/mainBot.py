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
    mess = f"Choose folder or write  number of preferable file \n {books.GetFilesList(message.text)}"
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


bot.polling(non_stop=True)
