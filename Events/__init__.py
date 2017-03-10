# -*- coding: utf-8 -*-


from datetime import datetime, timedelta
from random import randint

from Events.MetuEventsBridge import MetuEventsDb
from Helpers.RandomStringGenerator import randomString


class Events:
    def __init__(self):
        pass

    def getUpcomingEvents(self):
        db = MetuEventsDb()
        events = db.fetchAll()
        db.connection.close()

        upcomingEvents = []
        for event in events:
            del event["event_category"]
            del event["event_status"]
            del event["status"]
            #http://ncc.metu.edu.tr/sites/default/files/etkinlik-dugunumuz-var.jpg
            event["image_uri"] = event["image_uri"].replace("public://", "http://ncc.metu.edu.tr/sites/default/files/")

            if self._isLongerThan6Months(event):
                continue

            if event["son_tarih"] >= datetime.today():
                event["ilk_tarih"] = event["ilk_tarih"].isoformat()
                event["son_tarih"] = event["son_tarih"].isoformat()
                upcomingEvents.append(event)

        return upcomingEvents

    def getRawUpcomingEvents(self):
        db = MetuEventsDb()
        events = db.fetchAllRaw()
        db.connection.close()

        return events

    def getMockUpcomingEvents(self):
        upcomingEvents = []
        for eventCount in range(randint(2,10)):
            upcomingEvents.append(self._getMockEvent())
        return upcomingEvents

    def _getMockEvent(self):
        event = {}
        event['en_title'] = randomString()
        event['tr_title'] = randomString()
        event['en_location'] = randomString()
        event['tr_location'] = randomString()
        event['en_summary'] = randomString()
        event['tr_summary'] = randomString()
        event['date'] = datetime.today()
        event['date'] += timedelta(days=randint(0,1000))
        event['date'] = event['date'].isoformat()

        return event

    def _isLongerThan6Months(self, event):
        firstDate = event['ilk_tarih']
        lastDate = event['son_tarih']
        delta = lastDate - firstDate
        return True if delta.days>180 else False