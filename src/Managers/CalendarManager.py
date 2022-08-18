import config

def GetCalendarText():
        string = "-----------Write type-----------\n"
        count = 1
        for item in CalendarDIC.keys():
            string += str(count)  + "." + item  + "\n"
            count+=1
        string += "---------------------------------"
        return string
CalendarDIC = { 
        "day" : config.DayCalendarImage,
        "week" : config.WeekCalendarImage
         }