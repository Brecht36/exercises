# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
import re 
from abc import ABC, abstractmethod
class Person:
    @staticmethod
    def is_validname(name):
        return re.fullmatch("\w+ \w+( \w+)*", name)
    
    def __init__(self, id, name, is_a_student):
        if not self.is_valid_name(name):
            raise ValueError
        self.id = id
        self.is_a_student = is_a_student
        self.name = name

    @property
    def name (self):
        return self.__name
    
    @name.setter
    def name (self, name):
        if not self.is_valid_name(name):
            raise ValueError
        else:
            self.__name = name
    
class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupancts == dict()

    @property
    def number_of_occupants(self):
        return len(self.__occupants)
    
    @property 
    def maximum_occupants(self):
        return min(self.area//20, self.number_of_rooms*2)
    
    def register_resident(self, person):
        if not person.id in self.number_of_occupants:
            if self.number_of_occupants < self.maximum_occupants:
                self.__occupants[person.id] == person 
            else: 
                raise RuntimeError
            
    def unregistered_resident(self, id):
        if id in self.__occupants.keys():
            del self.__occupants[id]

    def resident_names(self):
        return [person.name for person in self.__occupants.values()]
    
    @abstractmethod
    def calculate_value():
        pass # of ...

class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity
    
    def calculate_value(self):
        return (self.number_of_rooms * 25000) + (2100 * self.area) + (10000 * self.garage_capacity)
    
class StudentKot(Residence):
    def __init__(self, address, area):
        super().__init__(address, area, 1)

    def register_resident(self, person):
        if not person.is_a_student:
            raise RuntimeError
        else: 
            super().register_resident(person)

    def calculate_value(self):
        return 150000 + (750 * self.area)

