class Control:
    
    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)
    
    
    def turnOff(self):
        self._tv.turnOff()
        

    def turnOn(self):
        self._tv.turnOn()
    
    
    def canalUp(self):
        if (self._tv._canal < 120 and self._tv._estado == True):
            self._tv.canalUp()

    def canalDown(self):
        if (self._tv._canal > 1 and self._tv._estado == True):
            self._tv.canalDown()

    
    def volumenUp(self):
        if (self._tv._volumen < 7 and self._tv._estado == True):
            self._tv.volumenUp()

    def volumenDown(self):
        if (self._tv._volumen > 0 and self._tv._estado == True):
            self._tv.volumenDown()

    def setCanal(self, canal):
        if (canal <= 120 and canal >= 1 and self._tv._estado == True):
            self._tv.setCanal(canal)

    def setVolumen(self, volumen):
        if (volumen <= 7 and volumen >= 0 and self._tv._estado == True):
            self._tv.setVolumen(volumen)

    def setTv(self, tv):
        self._tv = tv
    
    def getTv(self):
        return self._tv



    
        