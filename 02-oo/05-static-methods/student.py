class Duration:
    def __init__(self, *, time):
        self.__time = time

    @staticmethod
    def from_seconds(amount):
        return Duration(time=amount)

    @staticmethod
    def from_minutes(amount):
        return Duration(time=amount * 60)

    @staticmethod
    def from_hours(amount):
        return Duration(time=amount * 3600)

    @property
    def seconds(self):
        return self.__time

    @property
    def minutes(self):
        return self.__time / 60

    @property
    def hours(self):
        return self.__time / 3600
    
    
    