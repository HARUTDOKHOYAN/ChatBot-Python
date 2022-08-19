import FileFactory
import CalendarManager
from config import BotPatern

class PaternModel():
    def __init__(self , name ,text):
        self.Name = name
        self.Text = text
    def Detect(self, doc):
        return False 
class IntentPaternModel(PaternModel):
    def __init__(self, name, verbList, dobjList, text):
        super().__init__(name, text)
        self.VerbList = verbList
        self.DobjList = dobjList
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
class FilePaternModel(PaternModel):
    def __init__(self, name,text):
        super().__init__(name,  text)
    def Detect(self, doc):
        for token in doc:
            Path = FileFactory.GetFilePath(token.text)
            if token.dep_ == "dobj" and Path == None:
                for child in token.lefts:
                     if child.dep_ == 'amod' or child.dep_ == 'compound':
                         self.Text = FileFactory.GetFilePath(child.text)
                         if self.Text != None:
                            return True
            elif Path != None:
                 self.Text = Path
                 return True
        self.Text =  "Your File is not recognize"
        return  False 

def FindPatern(doc):
    for Patern in PaternsList:
        if(Patern.Detect(doc)):
            return Patern
    return PaternModel(BotPatern.FindPatern,'Your intent is not recognize.Try again or show List')

PaternsList = []

PaternsList.append(IntentPaternModel(
                              BotPatern.ListPatern,
                              ['take','want','give','get','show'], 
                              ['list','datalist','data','info','listinfo'],
                              FileFactory.GetChaptersLIst()
                              ))
PaternsList.append(IntentPaternModel(
                              BotPatern.CalendarPatern,
                              ['take','want','give','get','show'],
                              ['calendar','taskList'],
                              CalendarManager.GetCalendarText()
                              ))
PaternsList.append(FilePaternModel(
                              BotPatern.GetFilePatern,
                              'File'
                              ))