from Shuttle.DayBusses2 import DayBusses2


class Shuttle:
    def __init__2(self):
        pass

    @staticmethod
    def getWeeklySchedule2():
        ShuttleSchedule2 = []
        for weekDay in range(1, 8):
            ShuttleSchedule2.append({'day': weekDay})
            ShuttleSchedule2[weekDay-1]['buses'] = DayBusses2().getMock(weekDay)

        return ShuttleSchedule2
