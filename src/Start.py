import spacy  
import FileFactory
import PaternFactory
import CalendarManager
from config import BotPatern , TOKEN 
from telegram.ext import Updater , MessageHandler , Filters , ConversationHandler ,CommandHandler


nlp = spacy.load("en_core_web_md")

def StartBot(update , context):
    update.message.reply_text("""Hi
    Welcome to MiniStorage.
    My name is Supram.
    What do you want from storage?
    Оr you need a list of available dates?""")
    return BotPatern.FindPatern
def CancelBot(update , context):
    update.message.reply_text("Have a nice day")
    return ConversationHandler.END
def GetPatern(update , context):
    msg = update.message.text
    doc = nlp(msg)

    patern = PaternFactory.FindPatern(doc)
    if  patern.Name == BotPatern.FindPatern:
        update.message.reply_text("Your intent is not recognize.Try again")
        return patern.Name
    else:
        update.message.reply_text(patern.Text) 
        return patern.Name
def GetList(update , context):
    msg = update.message.text
    doc = nlp(msg)

    patern = PaternFactory.FindPatern(doc)
    if  patern.Name == BotPatern.FindPatern:
        if msg in FileFactory.DataChapters.keys():
             update.message.reply_text(FileFactory.DataChapters[msg].GetFilesList())
        else:
            update.message.reply_text("Write the number of the required date")    
            return BotPatern.ListPatern 
    else:
        update.message.reply_text(patern.Text) 
        return patern.Name
def GetCalendar(update , context):
    msg = update.message.text
    doc = nlp(msg)

    patern = PaternFactory.FindPatern(doc)
    if  patern.Name == BotPatern.FindPatern:
        if msg.lower() in CalendarManager.CalendarDIC.keys():
             update.message.reply_photo(photo=open(CalendarManager.CalendarDIC[msg], 'rb'))
        else:
            update.message.reply_text("Write the number of the required date")    
            return BotPatern.ListPatern 
    else:
        update.message.reply_text(patern.Text) 
        return patern.Name
    return BotPatern.FindPatern
def MainBot():
    updater = Updater(TOKEN,use_context=True)
    disp = updater.dispatcher
    conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', StartBot)],states=
    {
        BotPatern.FindPatern : [MessageHandler(Filters.text,GetPatern)],
        BotPatern.ListPatern : [MessageHandler(Filters.text,GetList)],
        BotPatern.CalendarPatern : [MessageHandler(Filters.text,GetCalendar)]
    },
    fallbacks=[CommandHandler('cancel',CancelBot)]
    )
    disp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

MainBot()