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
    
    #    def _getBrochureData(self):
        #return [
    #["Oryantasyon Programı", "https://guide.ncc.metu.edu.tr/oryantasyon_programi", "Orientation Program", "https://guide.ncc.metu.edu.tr/orientation_program"],
    #["Yapılacaklar Listesi", "https://ncc.metu.edu.tr/sites/default/files/Check-List-v4.pdf", "Check List", "https://guide.ncc.metu.edu.tr/check_list/"],
    #["İlk Yıl Öğrencileri İçin Broşür", "https://guide.ncc.metu.edu.tr/ilk_yil_brosuru", "Brochures For New Comers", "https://guide.ncc.metu.edu.tr/new_comers_brochures"]
    #]
    
    
    def _getBrochureData(self):
        return [
    #["Yüksek Lisans Oryantasyon Programı", "https://ncc.metu.edu.tr/sites/default/files/oryantaston_yukseklisans.pdf", "Orientation Program for Graduate Students", "https://ncc.metu.edu.tr/sites/default/files/oryantaston_yukseklisans.pdf"],
    ["Uluslararası ve A Level Öğrencileri İçin Oryantasyon Programı", "https://ncc.metu.edu.tr/sites/default/files/2020-2021-Summer-Orientation.pdf", "Orientation Program for Int. and A Level Stds.", "https://ncc.metu.edu.tr/sites/default/files/2020-2021-Summer-Orientation.pdf"],
    #["YKS Öğrencileri İçin Oryantasyon Programı", "https://ncc.metu.edu.tr/sites/default/files/oryantaston_trv4.pdf", "Orientation Program for YKS Students", "https://ncc.metu.edu.tr/sites/default/files/oryantaston_trv4.pdf"],
    ["Uluslararası ve A Level Öğrencileri İçin Yapılacaklar Listesi", "https://ncc.metu.edu.tr/sites/default/files/Checklist-Spring2020.pdf", "Check List International and A Level Students", "https://ncc.metu.edu.tr/sites/default/files/Checklist-Spring2020.pdf"],
    #["YKS Öğrencileri İçin Yapılacaklar Listesi", "https://ncc.metu.edu.tr/sites/default/files/Check-List-v4.pdf", "Check List for YKS Students", "https://ncc.metu.edu.tr/sites/default/files/Check-List-v4.pdf"],
    ["İlk Yıl Öğrencileri İçin Broşür (İngilizce)", "https://guide.ncc.metu.edu.tr/new_comers_brochures", "Broshures For New Comers in English", "https://guide.ncc.metu.edu.tr/new_comers_brochures"],
    ["İlk Yıl Öğrencileri İçin Broşür (Türkçe)", "https://guide.ncc.metu.edu.tr/ilk_yil_brosuru", "Broshures For New Comers in Turkish", "https://guide.ncc.metu.edu.tr/ilk_yil_brosuru"]
    ]
    
    

    def _recordToDict(self, record):
        dict = {}
        dict['tr_title'] = record[0]
        dict['tr_url'] = record[1]
        dict['en_title'] = record[2]
        dict['en_url'] = record[3]
        return dict
