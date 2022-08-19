import FileFactory
import CalendarManager
from config import BotPatern

class PaternModel():
    def __init__(self , name ,verbList,dobjList,text):
        self.Name = name
        self.VerbList = verbList
        self.DobjList = dobjList
        self.Text = text
    def Detect(self, doc):
            verb = ' '
            dobj = ' '
            for token in doc:
                if token.dep_ == "dobj":
                    verb = token.head.lemma_.lower()
                    dobj = token.lemma_.lower()
            if  verb == ' ' or dobj == ' ': return False
            elif(dobj in self.DobjList  and verb in self.VerbList): return True  
            else: return False 

def FindPatern(doc):
    for Patern in PaternsList:
        if(Patern.Detect(doc)):
            return Patern
    return PaternModel(BotPatern.FindPatern,[],[],'')

PaternsList = []

PaternsList.append(PaternModel(
                              BotPatern.ListPatern,
                              ['take','want','give','get','show'], 
                              ['list','datalist','data','info','listinfo'],
                              FileFactory.GetChaptersLIst()
                              ))
PaternsList.append(PaternModel(
                              BotPatern.CalendarPatern,
                              ['take','want','give','get','show'],
                              ['calendar','taskList'],
                              CalendarManager.GetCalendarText()
                              ))
PaternsList.append(PaternModel(
                              BotPatern.GetFilePatern,
                              ['take','want','give','get','show'],
                              FileFactory.GetAllFilesList(),
                              ' '
                              ))