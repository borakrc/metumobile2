# -*- coding: utf-8 -*-
from Config import Config


class Brochures:
    def __init__(self):
        pass

    def getBrochures(self):
        brochureRecords = []
        for record in self._getBrochureData():
            try:
                recordDict = self._recordToDict(record)
                brochureRecords.append(recordDict)
            except:
                pass
        return brochureRecords

    def _getBrochureData(self):
        return [
    ["test.jpg", "türkçe_title","türkçe_link", "ingilizce_title","ingilizce_link"],
    ]
    
    

    def _recordToDict(self, record):
        dict = {}
        dict['img'] = Config.serverRootLink +"/images/" + record[0]
        dict['tr_title'] = record[1]
        dict['tr_url'] = record[2]
        dict['en_title'] = record[3]
        dict['en_url'] = record[4]
        return dict
