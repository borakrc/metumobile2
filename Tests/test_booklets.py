from unittest import TestCase
from Booklets import Booklets

class TestBooklets(TestCase):
    def test_getBooklets(self):
        result = Booklets().getBooklets()
        assert isinstance(result, list)
        assert len(result) > 0

    def test__getBookletData(self):
        result = Booklets()._getBookletData()
        assert 'TELEFON' in result[0][1]

    def test__recordToDict(self):
        result = Booklets()._recordToDict(['academicbuildings.jpg',"AKADEMIK BLOKLAR","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/AKADEMIK-BLOKLAR-TR.pdf", "ACADEMIC BLOCKS", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/AKADEMIK-BLOKLAR-ENG.pdf"])
        assert result['tr_title'] == 'AKADEMIK BLOKLAR'
