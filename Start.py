from telegram.ext import Updater , MessageHandler , Filters , ConversationHandler ,CommandHandler
from config import BotState , TOKEN
import spacy  
import PaternFactory


def StartBot(update , context):
    update.message.reply_text("Hi welcome to MiniStorage.My name is Supram.What do you want from storage?")
    return BotState.FindPatern
def CancelBot(update , context):
    update.message.reply_text("Have a nice day")
    return ConversationHandler.END
def GetPatern(update , context):
    msg = update.message.text
    nlp = spacy.load("en_core_web_md")
    doc = nlp(msg)

    patern = PaternFactory.FindPatern(doc)
    if  patern == BotState.FindPatern:
        update.message.reply_text("Your intent is not recognize.Try again")
        return patern
    else: return patern
def MainBot():
    updater = Updater(TOKEN,use_context=True)
    disp = updater.dispatcher
    conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', StartBot)],states=
    {
        BotState.FindPatern : [MessageHandler(Filters.text,GetPatern)],
        BotState.ADD_INFO : [MessageHandler(Filters.text,Add_info)]
    },
    fallbacks=[CommandHandler('cancel',CancelBot)]
    )
    disp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

MainBot()