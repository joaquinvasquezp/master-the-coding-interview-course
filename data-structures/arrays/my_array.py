class MyArray:

    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)
        return item

    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        del self.data[self.length - 1]
        self.length -= 1

    def __str__(self):
        return str(self.__dict__)


my_array = MyArray()
my_array.push('hello')
my_array.push('world')
my_array.push('test')
my_array.push('rick')
my_array.push('and')
my_array.push('morty')
print(my_array)
print(my_array.get(1))
my_array.pop()
print(my_array)
my_array.delete(2)
print(my_array)