class DynamicArray:
    
    def __init__(self, capacity: int):
        self.__list = []
        self.__capacity = capacity
        self.__size = 0

    def get(self, i: int) -> int:
        return self.__list[i]

    def set(self, i: int, n: int) -> None:
        self.__list[i] = n

    def pushback(self, n: int) -> None:
        self.__list.append(n)
        if self.__size == self.__capacity:
            self.resize()
        self.__size += 1

    def popback(self) -> int:
        self.__size -= 1
        return self.__list.pop()

    def resize(self) -> None:
        self.__capacity *= 2

    def getSize(self) -> int:
        return self.__size
    
    def getCapacity(self) -> int:
        return self.__capacity
