class LinkedList:
    
    def __init__(self):
        self.__sll = []
    
    def get(self, index: int) -> int:
        if index >= len(self.__sll):
            return -1
        return self.__sll[index]

    def insertHead(self, val: int) -> None:
        self.__sll = [val] + self.__sll

    def insertTail(self, val: int) -> None:
        self.__sll.append(val)

    def remove(self, index: int) -> bool:
        if index >= len(self.__sll):
            return False
        del self.__sll[index]
        return True

    def getValues(self) -> List[int]:
        return self.__sll
