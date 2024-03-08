from libraryitem import Book, CD, Strip
from genre import Genre
from id_util import Id_Util

items = []

class Library():

    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        print(f'"{item.title}" has been added to the library.')
        self.items.append(item)

    def check_out_item(self, id):
        for item in self.items:
            if item.id == id:
                if item.status:
                    item.status = False
                else:
                    print('Item not verkrijgbaar in de library!')
                return
        print(f'Unknown item with id {id}')

    def print_library(self):
        print("The library contains:")
        print(len(self.items))
        for item in self.items:
            print(f"{item.id}, {item.title}, {item.status}")

book = Book("De leeuw", "Henry", Id_Util.generate_id(), True, Genre.FICTION)
cd = CD("Master ...", "Metallica", Id_Util.generate_id(), True, 500)
strip = Strip("De jacht op een voetbal", "Jef Nijs", Id_Util.generate_id(), True, 1)

library = Library()

library.add_item(book)
library.add_item(cd)
library.add_item(strip)

library.print_library()