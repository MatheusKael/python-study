

class Jar:

    def __init__(self, capacity=12):

        if capacity < 0:
            raise ValueError

        self.__capacity = capacity
        self.cookie_jar = []

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError
        for i in range(n):
            self.cookie_jar.append("🍪")

        self.size = n

    def withdraw(self, n):

        if n > self.size:
            raise ValueError

        for i in range(n):
            self.cookie_jar.pop()

    @property
    def capacity(self):

        return self.__capacity

    @property
    def size(self):
        return self.__size


def main():
    jar = Jar()

    print(jar.capacity)


main()
