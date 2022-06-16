"""
Пользователь вводит два числа N и M, рассчитать последовательность  N + NN + NNN + ... + NxM.
"""
class Symbols:
    def __init__(self, symbol: str, count: int):
        self.symbol = symbol
        self.current_value = symbol
        self.count = count


    def __next__(self):
        previous_value = self.current_value
        if len(self.current_value) <= self.count:
            self.current_value += self.symbol
            return previous_value
        else:
            raise StopIteration

    def __iter__ (self):
        self.current_value = self.symbol
        return self

if __name__ == "__main__":
    my_sum = Symbols(symbol="N", count=7)
    for item in my_sum:
        print(item)