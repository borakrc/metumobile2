# -*- coding: utf-8 -*-


class DayBusses2(object):
    @staticmethod
    def getMock(dayType):
        dailyBuses = []
        
        if dayType == 0:
             for hour in [10, 12, 14, 16, 18, 20, 22, 23]:
                bus = {'index': 0, 'price': 0.95, 'tr_destination': 'ODTU KKK', 'en_destination': 'METU NCC',
                       'stops': [{"hour": hour, "minute": 5, "tr_name": "Terminal", "en_name": "Terminal"}]}
                dailyBuses.append(bus)

                bus = {'index': 0, 'price': 0.95, 'tr_destination': 'Terminal', 'en_destination': 'Terminal',
                   'stops': [{"hour": hour, "minute": 45, "tr_name": "2. Yurt", "en_name": "2nd Dormitory"}
                             ]}
                dailyBuses.append(bus)
            return dailyBuses
        
        elif dayType == 1:          
                for hour in [10, 12, 14, 16, 18, 20, 22, 23]:
                bus = {'index': 0, 'price': 0.95, 'tr_destination': 'ODTU KKK', 'en_destination': 'METU NCC',
                       'stops': [{"hour": hour, "minute": 5, "tr_name": "Terminal", "en_name": "Terminal"}]}
                dailyBuses.append(bus)

                bus = {'index': 0, 'price': 0.95, 'tr_destination': 'Terminal', 'en_destination': 'Terminal',
                   'stops': [{"hour": hour, "minute": 45, "tr_name": "2. Yurt", "en_name": "2nd Dormitory"}
                             ]}
                dailyBuses.append(bus)
            return dailyBuses
        else:
            return dailyBuses
