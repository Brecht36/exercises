# Write your code here
# Voor setter geen private field in initiator

# class Person:
#     def __init__(self, age):
#         self.__age = age

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, value):
#         ???

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self, value):
        if 0 <= value <= 23:
            self.__hours = value
        else:
            raise ValueError("Error")

    @property
    def minutes(self):
        return self.__minutes
    @minutes.setter
    def minutes(self, value):
        if 0 <= value <= 59:
            self.__minutes = value
        else:
            raise ValueError("Error")
        
    
    @property
    def seconds(self):
        return self.__seconds
    @seconds.setter
    def seconds(self, value):
        if 0 <= value <= 59:
            self.__seconds = value
        else:
            raise ValueError("Error")
    