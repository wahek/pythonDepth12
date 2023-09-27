class Descriptor:
    def __set_name__(self, owner, name):
        self.__param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.__param_name)

    def __set__(self, instance, value):
        self.valid(value)
        setattr(instance, self.__param_name, value)

    @staticmethod
    def valid(value):
        if value < 0:
            raise ValueError('нет')


class Factorial:
    __start = Descriptor()
    __stop = Descriptor()
    __step = Descriptor()
    # __slots__ = ('__start', '__stop', '__step')

    def __init__(self, stop, start=1, step=1):
        self.__start = start
        self.__stop = stop
        self.__step = step

    def __iter__(self):
        return self

    def __next__(self):
        while self.__stop >= self.__start:
            res = 1
            for i in range(1, self.__start):
                res *= i
            self.__start += 1
            return res
        raise StopIteration


if __name__ == '__main__':
    a = Factorial(7, 2, 4)
    for i in a:
        print(i)
    a = Factorial(10)
    for k in a:
        print(k)

    a.start = 2
    print(a.start)
