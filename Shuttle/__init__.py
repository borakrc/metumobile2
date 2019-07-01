from Shuttle.DayBusses import DayBusses
from Shuttle.DayBusses2 import DayBusses2


class Shuttle:
    def __init__(self):
        pass

    @staticmethod
    def getWeeklySchedule():
        ShuttleSchedule = []
        for weekDay in range(1, 8):
            ShuttleSchedule.append({'day': weekDay})
            ShuttleSchedule[weekDay-1]['buses'] = DayBusses().getMock(weekDay)

        return ShuttleSchedule
    @staticmethod
    def getWeeklySchedule2():
        ShuttleSchedule2 = []
        for dayType in range(1, 3):
             ShuttleSchedule2.append({'day': (dayType-1)}) 
             ShuttleSchedule2[dayType-1]['buses']=(DayBusses2().getMock(dayType-1))
            
             ShuttleSchedule2[0].append('warning_message': 1)
             ShuttleSchedule2[1].append('warning_message': 1)      
               
        return ShuttleSchedule2
