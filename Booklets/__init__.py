# -*- coding: utf-8 -*-
from Config import Config


class Booklets:
    def __init__(self):
        pass

    def getBooklets(self):
        bookletRecords = []
        for record in self._getBookletData():
            try:
                recordDict = self._recordToDict(record)
                bookletRecords.append(recordDict)
            except:
                pass
        return bookletRecords

    def _getBookletData(self):
        return [
    ["survival_turkish.jpg", "SURVIVAL TURKISH FOR INTERNATIONAL STUDENTS ON CAMPUS","https://intranet.ncc.metu.edu.tr/files/SurvivalTurkish.pdf", "SURVIVAL TURKISH FOR INTERNATIONAL STUDENTS ON CAMPUS","https://intranet.ncc.metu.edu.tr/files/SurvivalTurkish.pdf"],
    ["defaultbookletpicture.jpg", "ÇEVRE TELEFON REHBERİ","https://intranet.ncc.metu.edu.tr/files/CEVRE_TELEFON_REHBERI_TR.pdf", "PHONE GUIDE","https://intranet.ncc.metu.edu.tr/files/CEVRE_TELEFON_REHBERI_ENG.pdf"],
    ["food.jpg", "MERKEZ KAFETERYA VE KANTİNLER","https://intranet.ncc.metu.edu.tr/files/KAFETERYA-TR.pdf", "MAIN CAFETERIA AND CANTEENS", "https://intranet.ncc.metu.edu.tr/files/KAFETERYA-ENG.pdf"],
    ["health.jpg", "MEDİKO","https://intranet.ncc.metu.edu.tr/files/mediko-elkitabi.pdf", "MEDICO", "https://intranet.ncc.metu.edu.tr/files/medico-healthcare-guide.pdf"],
    ["sports.jpg", "SPOR TESİSLERİ","https://intranet.ncc.metu.edu.tr/files/SPOR-MERKEZI-TR.pdf", "SPORTS AND RECREATION", "https://intranet.ncc.metu.edu.tr/files/SPOR-MERKEZI-ENG.pdf"],
    ["kkm.jpg", "KÜLTÜR VE KONGRE MERKEZİ","https://intranet.ncc.metu.edu.tr/files/KULTUR-VE-KONGRE-MERKEZI-TR.pdf", "CULTURE AND CONVENTION CENTER", "https://intranet.ncc.metu.edu.tr/files/KULTUR-VE-KONGRE-MERKEZI-ENG.pdf"],
    ["library.jpg", "KÜTÜPHANE","https://intranet.ncc.metu.edu.tr/files/KUTUPHANE-TR.pdf", "LIBRARY", "https://intranet.ncc.metu.edu.tr/files/KUTUPHANE-ENG.pdf"],
    ["dorm.jpg", "YURTLAR","https://intranet.ncc.metu.edu.tr/files/YURTLAR-TR.pdf", "DORMITORIES", "https://intranet.ncc.metu.edu.tr/files/YURTLAR-ENG.pdf"],
    ["academicbuildings.jpg", "AKADEMİK BLOKLAR","https://intranet.ncc.metu.edu.tr/files/AKADEMIK-BLOKLAR-TR.pdf", "ACADEMIC BLOCKS", "https://intranet.ncc.metu.edu.tr/files/AKADEMIK-BLOKLAR-ENG.pdf"],
    ["technicalservices.jpg", "TEKNİK HİZMETLER","https://intranet.ncc.metu.edu.tr/files/TEKNIK-HIZMETLER-KILAVUZU-TR.pdf", "TECHNICAL SERVICES GUIDE", "https://intranet.ncc.metu.edu.tr/files/TEKNIK-HIZMETLER-KILAVUZU-ENG.pdf"],
    ["it.jpg", "BİLİŞİM TEKNİKLERİ","https://intranet.ncc.metu.edu.tr/files/BILISIM-TEKNIKLERI-KILAVUZU-1-TR.pdf", "TECHNICAL GUIDE FOR IT SERVICES 1", "https://intranet.ncc.metu.edu.tr/files/BILISIM-TEKNIKLERI-KILAVUZU-1-ENG.pdf"],
    ["it.jpg", "BİLİŞİM TEKNİKLERİ-2","https://intranet.ncc.metu.edu.tr/files/BILISIM-TEKNIKLERI-KILAVUZU-2-TR.pdf", "TECHNICAL GUIDE FOR IT SERVICES 2", "https://intranet.ncc.metu.edu.tr/files/BILISIM-TEKNIKLERI-KILAVUZU-2-ENG.pdf"],
    ["administrativeservices.jpg", "İDARİ HİZMET VE KURALLAR","https://intranet.ncc.metu.edu.tr/files/IDARI-HIZMET-VE-KURALLAR-1-TR.pdf", "ADMINISTRATIVE SERVICES AND RULES 1", "https://intranet.ncc.metu.edu.tr/files/IDARI-HIZMET-VE-KURALLAR-1-ENG.pdf"],
    ["administrativeservices.jpg", "İDARİ HİZMET VE KURALLAR-2","https://intranet.ncc.metu.edu.tr/files/IDARI-HIZMET-VE-KURALLAR-2-TR.pdf", "ADMINISTRATIVE SERVICES AND RULES 2", "https://intranet.ncc.metu.edu.tr/files/IDARI-HIZMET-VE-KURALLAR-2-ENG.pdf"],
    ["administrativeservices.jpg", "İDARİ HİZMET VE KURALLAR-3","https://intranet.ncc.metu.edu.tr/files/IDARI-HIZMET-VE-KURALLAR-3-TR.pdf", "ADMINISTRATIVE SERVICES AND RULES 3", "https://intranet.ncc.metu.edu.tr/files/IDARI-HIZMET-VE-KURALLAR-3-ENG.pdf"],
    ["guest.jpg", "MİSAFİRHANE", "https://intranet.ncc.metu.edu.tr/files/MISAFIRHANE-TR.pdf", "GUEST HOUSE", "https://intranet.ncc.metu.edu.tr/files/MISAFIRHANE-ENG.pdf"],
    ["defaultbookletpicture.jpg", "YEŞİL KAMPUS", "https://intranet.ncc.metu.edu.tr/files/YESIL-KAMPUS-TR.pdf", "GREEN CAMPUS", "https://intranet.ncc.metu.edu.tr/files/YESIL-KAMPUS-ENG.pdf"],
    ["defaultbookletpicture.jpg", "TRAFİK KURALLARI", "https://intranet.ncc.metu.edu.tr/files/trafik_kurallari_TR.pdf", "TRAFFIC REGULATIONS", "https://intranet.ncc.metu.edu.tr/files/trafik_kurallari_ENG.pdf"],
    ["defaultbookletpicture.jpg", "İS SAGLIĞI VE GÜVENLİĞİ", "https://intranet.ncc.metu.edu.tr/files/IS-SAGLIGI-VE-GUVENLIGI-TR.pdf", "OCCUPATIONAL HEALTH AND SAFETY", "https://intranet.ncc.metu.edu.tr/files/IS-SAGLIGI-VE-GUVENLIGI-ENG.pdf"],
    ["technicalservices.jpg", "1. YURT TEKNİK KILAVUZU", "https://intranet.ncc.metu.edu.tr/files/1-YURT-TEKNIK-KILAVUZU-TR.pdf", "TECHNICAL GUIDELINES DORM I", "https://intranet.ncc.metu.edu.tr/files/1-YURT-TEKNIK-KILAVUZU-ENG.pdf"],
    ["technicalservices.jpg", "2. YURT TEKNİK KILAVUZU", "https://intranet.ncc.metu.edu.tr/files/2-YURT-TEKNIK-KILAVUZU-TR.pdf", "TECHNICAL GUIDELINES DORM II", "https://intranet.ncc.metu.edu.tr/files/2-YURT-TEKNIK-KILAVUZU-ENG.pdf"],
    ["technicalservices.jpg", "3. YURT TEKNİK KILAVUZU", "https://intranet.ncc.metu.edu.tr/files/3-YURT-TEKNIK-KILAVUZU-TR.pdf", "TECHNICAL GUIDELINES DORM III", "https://intranet.ncc.metu.edu.tr/files/3-YURT-TEKNIK-KILAVUZU-ENG.pdf"],
    ["defaultbookletpicture.jpg", "ÖĞRENCİ GELİŞİM VE PSİKOLOJİK DANIŞMA MERKEZİ", "https://intranet.ncc.metu.edu.tr/files/OGRENCI-GEL-VE-PSI-DANIS-MRK-TR-1.pdf", "STUDENT DEVELOPMENT AND COUNSELING CENTER", "https://intranet.ncc.metu.edu.tr/files/OGRENCI-GEL-VE-PSI-DANIS-MRK-ENG-.pdf"]
    ]
    
    

    def _recordToDict(self, record):
        dict = {}
        dict['img'] = Config.serverRootLink +"/images/" + record[0]
        dict['tr_title'] = record[1]
        dict['tr_url'] = record[2]
        dict['en_title'] = record[3]
        dict['en_url'] = record[4]
        return dict
