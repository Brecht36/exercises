from abc import ABC, abstractmethod

class LibraryItem(ABC):

    def __init__(self, title, author, id, status):
        self.title = title
        self.author = author
        self.id = id
        self.status = status

    @abstractmethod
    def check_status(self):
        pass

class Book(LibraryItem):

    def __init__(self, title, author, id, status, genre):
        super().__init__(title, author, id, status)
        self.genre = genre

    def check_status(self):
        feedback = input('Are all pages present? (Y/N):')
        if feedback == 'N':
            print("A fine needs to be payed: 10 euro")

class CD(LibraryItem):

    def __init__(self, title, author, id, status, tracks):
        super().__init__(title, author, id, status)
        self.tracks = tracks

    def check_status(self):
        feedback = input('Is CD present? (Y/N):')
        if feedback == 'N':
            print("A fine needs to be payed: 50 euro")

class Strip(LibraryItem):

    def __init__(self, title, author, id, status, issueNumber):
        super().__init__(title, author, id, status)
        self.issueNumber = issueNumber
        
    def check_status(self):
        feedback = input('Are all pages present? (Y/N):')
        if feedback == 'N':
            print("A fine needs to be payed: 10 euro")
