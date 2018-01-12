# -*- coding: utf-8 -*-


class DayBusses2(object):
    @staticmethod
    def getMock(weekDay):
        dailyBuses = []

        if weekDay <= 7:
            for hour in [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 00]:
                bus = {'index': 0, 'price': 0.95, 'tr_depart_from' : 'Terminal', 'en _depart_from' : 'Terminal', 
                       'tr_destination': 'ODTU KKK', 'en_destination': 'METU NCC', 'departure_hour': hour,
                       'departure_minute': 5, 'arrive_hour': hour, 'arrive_minute': 45 }
                      
                dailyBuses.append(bus)
                
                bus = {'index': 0, 'price': 0.95, 'tr_depart_from' : 'ODTU KKK', 'en _depart_from' : 'METU NCC', 
                       'tr_destination': 'Terminal', 'en_destination': 'Terminal', 'departure_hour': hour,
                       'departure_minute': 45, 'arrive_hour': hour+1 , 'arrive_minute': 5 }
                dailyBuses.append(bus)

        return dailyBuses
