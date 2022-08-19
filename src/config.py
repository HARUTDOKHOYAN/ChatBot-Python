import sys
from enum import Enum

sys.path.insert(1, ".\src\Factorys")
sys.path.insert(1, "./Managers")


TOKEN = 'SetUp ID'
DayCalendarImage = ""
WeekCalendarImage = ""
class BotPatern (Enum):
    FindPatern = 1
    ListPatern = 2
    CalendarPatern = 3 
    GetFilePatern = 4