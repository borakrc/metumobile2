# -*- coding: utf-8 -*-

from MetuPhonebookBridge import PhonebookBridge


class Phonebook:
    def __init__(self):
        pass

    def _getPhonebookRecordsFromMetuDb(self):
        rawDbResult = PhonebookBridge().fetchAllFromDb()
        activePhonebookRecords = []
        for eachRecord in rawDbResult:
            if eachRecord['durum'] == "aktif":
                recordDict = {}
                recordDict['title'] = eachRecord['title']
                recordDict['id'] = eachRecord['id']
                recordDict['pinned'] = False
                name = eachRecord['name']
                if name[0] == " " or name[0] == "!":
                    name = name[1:]
                    recordDict['pinned'] = True
                recordDict['name'] = name
                recordDict['surname'] = eachRecord['surname']
                recordDict['position'] = eachRecord['position']
                recordDict['officeTel'] = eachRecord['oftelno']
                recordDict['unit'] = eachRecord['unit']
                recordDict['officeLocation'] = eachRecord['ofno']
                if eachRecord['email']:
                    try:
                        recordDict['email'] = str(eachRecord['email']) + "@metu.edu.tr"
                    except:
                        recordDict['email'] = None
                else:
                    recordDict['email'] = None
                    
                if eachRecord['resno']:
                    try:
                        recordDict['resno'] = str(eachRecord['resno'])
                    except:
                        recordDict['resno'] = None
                else:
                    recordDict['resno'] = None
                    
                if eachRecord['restel']:
                    try:
                        recordDict['restel'] = str(eachRecord['restel'])
                    except:
                        recordDict['restel'] = None
                else:
                    recordDict['restel'] = None
                    
                activePhonebookRecords.append(recordDict)

        return activePhonebookRecords

    def getRawPhonebookRecords(self):
        rawDbResult = PhonebookBridge().fetchAllFromDb()
        for each in rawDbResult:
            each['resno'] = "conf."
            each['restel'] = "conf."
            each['sicilno'] = "conf."
        return rawDbResult

    def _getStaticRecords(self):
        phonebookRecords = []
        for record in self._getPhonebookData():
            try:
                recordDict = self._recordToDict(record)
                phonebookRecords.append(recordDict)
            except:
                pass
        return phonebookRecords

    def getPhonebookRecords(self):
        return self._getPhonebookRecordsFromMetuDb()

    def _getPhonebookData(self):
        return []

    def _recordToDict(self, record):
        recordDict = {}
        recordDict['title'] = record[0]
        recordDict['name'] = record[1]
        recordDict['surname'] = record[2]
        recordDict['position'] = record[3]
        recordDict['officeTel'] = record[4]
        recordDict['unit'] = record[5]
        return recordDict
