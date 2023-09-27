import json


class Fibbo:

    def __init__(self,number:int):
        self._number = number
        self._archive = []

    @property
    def archive(self):
        return self._archive

    def __call__(self, num:int):
        res = 1
        for i in range(2, num+1):
            res *= i
        if len(self._archive) > self._number:
            self._archive.pop(0)
        self._archive.append({num: res})
        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('json.json', 'w', encoding='UTF-8') as file:
            json.dump(self.archive, file, indent=4)

if __name__ == '__main__':
    t1 = Fibbo(10)
    print(t1.archive)
    print(t1(22))
    print(t1(7))
    print(t1.archive)
    with t1 as f:
        f(5)
        f(6)
        f(7)
        f(8)
        f(9)
