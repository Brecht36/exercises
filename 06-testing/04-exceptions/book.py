class Book:
    def __init__(self, title, isbn):
        if Book.check_title(title): # type: ignore
            raise RuntimeError("Title must not be empty.")
        if not Book.check_isbn(isbn):
            raise RuntimeError("ISBN must be valid format.")
            
        self.__title = title
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @property
    def isbn(self):
        return self.__isbn
    
    # @title.setter
    @staticmethod
    def check_title(value):
        return len(value) <= 0
        

    @staticmethod
    def check_isbn(value):
        numbers = [int(i) for i in value if '0' <= i <= '9']
        if len(numbers) !=13 and len(value) != 14:
            return False
        list = [1,3,5,7,9,11]
        new_numbers = []
        for x, i in enumerate(numbers):
            if x in list:
                i = i * 3
            new_numbers.append(i)
        # print(sum(new_numbers) % 10)
        return sum(new_numbers) % 10 == 0



# isbn_checker("978-1779501126")

