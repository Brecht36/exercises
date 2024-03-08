class CircularBuffer:
    def __init__(self, n):
        self.__n = n
        self.__li = []

    def __len__(self):
        return len(self.__li)
    
    def __getitem__(self, index):
        return self.__li[index]
    
    def add(self, item):
        self.__li.append(item)
        if (len(self.__li) > self.__n):
            del self.__li[0]
        
        

