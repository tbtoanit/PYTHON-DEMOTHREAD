#new version 46622
class KhachHang:
    _maKH = ""
    _tenKH = ""
    _diaChi = ""
    _sdt = ""
    _level = ""

    def setMaKH(self, id):
        self._maKH = id

    def getMaKH(self):
        return self._maKH

    def setTenKH(self, name):
        self._tenKH = name

    def getTenKH(self):
        return self._tenKH

    def setDiaChi(self, address):
        self._tenKH = address

    def getDiaChi(self):
        return self._diaChi

    def setLevel(self, level):
        self._level = level

    def getLevel(self):
        return self._level

