class Stack:
    def __init__(self):
        self.__storage = []
        self.size = 0
        self.__isEmpty = True

    @property
    def isEmpty(self):
        return self.__isEmpty

    def push(self, value):
        self.__storage.append(value)
        if self.size == 0:
            self.__isEmpty = False
        self.size += 1

    def peak(self):
        if self.size > 0:
            return self.__storage[-1]
        else:
            return None

    def pop(self):
        if self.size > 0:
            self.size -= 1
        else:
            return -1
        
        if self.size == 0:
            self.__isEmpty = True

        return self.__storage.pop()

    def __len__(self):
        return self.size

test = Stack()
[print(f"is stack empty? {test.isEmpty}")]

test.push(3)
test.push(1)
test.push(4)
print(len(test))
print(f"Peeking our test stack: {test.peak()}")
first_dish = test.pop()
print(f"Our fist pop: {first_dish}")
print(f"Peeking our test stack: {test.peak()}")