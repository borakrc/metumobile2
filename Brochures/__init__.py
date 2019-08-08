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
    ["Oryantasyon Programı", "https://guide.ncc.metu.edu.tr/oryantasyon_programi", "Orientation Program", "https://guide.ncc.metu.edu.tr/orientation_program"],
    ["Yapılacaklar Listesi", "https://guide.ncc.metu.edu.tr/yapilacaklar_listesi/", "Check List", "https://guide.ncc.metu.edu.tr/check_list/"],
    ["İlk Yıl Öğrencileri İçin Broşür", "https://guide.ncc.metu.edu.tr/ilk_yil_brosuru", "Brochures For New Comers", "https://guide.ncc.metu.edu.tr/new_comers_brochures"]
    ]
    
    

    def _recordToDict(self, record):
        dict = {}
        dict['tr_title'] = record[1]
        dict['tr_url'] = record[2]
        dict['en_title'] = record[3]
        dict['en_url'] = record[4]
        return dict
