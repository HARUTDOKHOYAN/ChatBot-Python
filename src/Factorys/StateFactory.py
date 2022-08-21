import FileFactory
import CalendarManager
from config import BotState ,HelpText

class StatePaternBase():
    def __init__(self , name ,text):
        self.Name = name
        self.Text = text
    def Detect(self, doc):
        return False 

class IntentStatePatern(StatePaternBase):
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

class FileStatePatern(StatePaternBase):
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

# API to find state using spacy doc
def FindState(doc):
    for Patern in PaternsList:
        if(Patern.Detect(doc)):
            return Patern
    return StatePaternBase(BotState.FindState,'Your intent is not recognize.Try again or show List')

PaternsList = []

PaternsList.append(IntentStatePatern(
                              BotState.FindListState,
                              ['take','want','give','get','show'], 
                              ['list','datalist','data','info','listinfo'],
                              FileFactory.GetChaptersLIst()
                              ))
PaternsList.append(IntentStatePatern(
                              BotState.FindCalendarState,
                              ['take','want','give','get','show'],
                              ['calendar','taskList'],
                              CalendarManager.GetCalendarText()
                              ))
PaternsList.append(IntentStatePatern(
                             BotState.FindState,
                             ['want'],
                             ['help'],
                             HelpText
                             ))
PaternsList.append(FileStatePatern(
                              BotState.GetFileState,
                              'File'
                              ))