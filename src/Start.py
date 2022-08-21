from config import BotState , TOKEN 
import spacy  
import FileFactory
import StateFactory
import CalendarManager
from telegram.ext import Updater , MessageHandler , Filters , ConversationHandler ,CommandHandler


nlp = spacy.load("en_core_web_md")
# Changes bot Stait
def SwitchState(update ,patern):
    if patern.Name == BotState.GetFileState:
         if patern.Text != "Your File is not recognize":
                 file = open(patern.Text , mode='rb',)
                 update.message.reply_text('Your file is coming.Thanks for wait')
                 update.message.reply_document(file)
         else:
             update.message.reply_text(patern.Text)
         return BotState.FindState
    else:
        update.message.reply_text(patern.Text) 
        return patern.Name

# BotStaits Metods

def StartBot(update , context):
    update.message.reply_text("""Hi
    Welcome to MiniStorage.
    My name is Supra01.
    What do you want from storage or calendar?
    Оr you need a list of available dates?""")
    update.message.reply_text('If you want help write <<I want help>>.')
    return BotState.FindState

def FindState(update , context):
    msg = update.message.text
    doc = nlp(msg)
    patern = StateFactory.FindState(doc)
    return SwitchState(update , patern)

def FindList(update , context):
    msg = update.message.text
    doc = nlp(msg)

    patern = StateFactory.FindState(doc)
    if  patern.Name == BotState.FindState:
        if msg in FileFactory.DataChapters.keys():
            global  datalist 
            datalist = FileFactory.DataChapters[msg]
            update.message.reply_text(datalist.GetFilesList())
            return BotState.GetFileState
        else:
            update.message.reply_text("Your intent is not recognize.\n Write the number of the required date")    
            return BotState.FindListState 
    return SwitchState(update , patern)

def FindCalendar(update , context):
    msg = update.message.text
    doc = nlp(msg)
    patern = StateFactory.FindState(doc)

    if  patern.Name == BotState.FindState:
        if msg.lower().capitalize() in CalendarManager.CalendarDIC.keys():
             update.message.reply_text('Your file is coming .  Thanks for wait')
             update.message.reply_photo(photo=open(CalendarManager.CalendarDIC[msg], 'rb'))
        else:
            update.message.reply_text("Your intent is not recognize.\n Write the type of the required date")    
            return BotState.FindCalendarState 
    return SwitchState(update , patern)

def GetFile(update , context):
     msg = update.message.text
     doc = nlp(msg)
     patern = StateFactory.FindState(doc)
     values = list(datalist.FilesList.values())

     if  patern.Name == BotState.FindState:
        try:   
            index = int(msg) -1
            update.message.reply_text('Your file is coming .  Thanks for wait')
            file = open(values[index] , mode='rb',)
            update.message.reply_document(file)
            return BotState.FindState
        except:
            update.message.reply_text("Your intent is not recognize.\n Write the number of the required date")
            return BotState.GetFileState
     return SwitchState(update , patern)

def EndBot(update , context):
    update.message.reply_text("Have a nice day")
    return ConversationHandler.END   

# Main bot function   
def MainBot():
    updater = Updater(TOKEN,use_context=True)
    disp = updater.dispatcher
    # Register Chat Handlers 
    conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', StartBot)],states=
    {
        BotState.FindState         : [MessageHandler(Filters.text,FindState)],
        BotState.FindListState     : [MessageHandler(Filters.text,FindList)],
        BotState.FindCalendarState : [MessageHandler(Filters.text,FindCalendar)],
        BotState.GetFileState      : [MessageHandler(Filters.text,GetFile)]
    },
    fallbacks=[CommandHandler('cancel',EndBot)]
    )
    disp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

MainBot()