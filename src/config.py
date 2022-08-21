import sys
from enum import Enum

sys.path.insert(1, "C:/Cragravorum/PYTHON/NLP/ChatBot/Factorys")
sys.path.insert(1, "C:/Cragravorum/PYTHON/NLP/ChatBot/Managers")


TOKEN = '5581007276:AAGGEa2ZURxijMdm2uD3MPPRlBmeOv9bDrc'
DayCalendarImage = "C:\Test.jpg"
WeekCalendarImage = ""
HelpText = "Hi.Тo communicate with the bot you need to use these verbs \n 'take , want , give , get , show'\n Example` \n \t \t I want List \n \t \t Give me list \n \t \t I want to give List \n  Оr write a number if iti present"


class BotState (Enum):
    FindState = 1
    FindListState = 2
    FindCalendarState = 3 
    GetFileState = 4