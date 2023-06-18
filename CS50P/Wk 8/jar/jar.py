#01/06/2023
#CS50P Week 8

'''
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._size = 0
        self._capacity = capacity

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

'''
class Jar:

    def __init__(self, capacity=12):
        self._size = 0
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if not (0 <=  n <= self._capacity):
            raise ValueError
        self._size = self._size + n

jar = Jar()
jar.deposit(0.5)
print(jar.size)
jar.deposit(0.5)
print(jar.size)
jar.deposit(0.5)
print(jar.size)
jar.withdraw(0.5)
print(jar.size)
jar.withdraw(0.5)
print(jar.size)
