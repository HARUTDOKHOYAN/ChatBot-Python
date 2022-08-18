from enum import Enum
import sys


sys.path.insert(1, "C:/Cragravorum/PYTHON/NLP/ChatBot/Factorys")
sys.path.insert(1, "C:/Cragravorum/PYTHON/NLP/ChatBot/Managers")


TOKEN = ''
DayCalendarImage = ""
WeekCalendarImage = ""
class BotPatern (Enum):
    FindPatern = 1
    ListPatern = 2
    CalendarPatern = 3 