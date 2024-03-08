class LengthConverter:
    inches = 39.3701
    foot = 3.28084
    
    def __init__(self):
        self.__meters = 0
    
    @property
    def meter(self):
        return self.__meters
    
    @meter.setter
    def meter(self, value):
        self.__meters = value

    @property
    def feet(self):
        return self.__meters * LengthConverter.foot
    
    @feet.setter
    def feet(self, value):
        self.__meters = value / LengthConverter.foot

    @property
    def inch(self):
        return self.__meters * LengthConverter.inches
    
    @inch.setter
    def inch(self, value):
        self.__meters = value / LengthConverter.inches
    