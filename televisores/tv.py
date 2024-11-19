
class TV: 
    _numTV = 0 
    
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None 
        self.totalTv()
        
    @classmethod
    def totalTv(cls):
        cls._numTV += 1
    
    def setMarca(self, marca):
        self._marca = marca

    def getMarca(self):
        return self._marca

        
    def setCanal(self, canal):
        if (canal <= 120 and canal >= 1 and self._estado == True):
            self._canal = canal

    def getCanal(self):
        return self._canal

        
    def setPrecio(self, precio):
        self._precio = precio

    def getPrecio(self):
        return self._precio
        
        
    def setVolumen(self, volumen):
        if (volumen <= 7 and volumen >= 0 and self._estado == True):
            self._volumen = volumen

    def getVolumen(self):
        return self._volumen

        
    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control
        

    def setNumTV(numtv):
        TV._numTV = numtv

    def getNumTV():
        return TV._numTV


    def turnOff(self):
        self._estado = False

    def turnOn(self):
        self._estado = True

    def getEstado(self):
        return self._estado

    def canalUp(self):
        if (self._canal < 120 and self._estado == True):
            self._canal += 1

    def canalDown(self):
        if (self._canal > 1 and self._estado == True):
            self._canal -= 1

    def volumenUp(self):
        if (self._volumen < 7 and self._estado == True):
            self._volumen += 1

    def volumenDown(self):
        if (self._volumen > 0 and self._estado == True):
            self._volumen -= 1

    