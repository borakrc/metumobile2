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
        Schedule2 = []
        for dayType in range(1, 3):
            for weekDay in range(1, 8):
                Schedule2.append({'day': weekDay})
                Schedule2[weekDay-1]['buses'] = DayBusses2().getMock(weekDay)
            
            ShuttleSchedule2[dayType-1]=({'schedule': Schedule2})
            ShuttleSchedule2.append({'holiday': dayType})
           
          
        return ShuttleSchedule2
