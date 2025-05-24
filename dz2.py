class PowerOfTwoIterator:
    def __init__(self, max_exponent=None):
        self.exponent = 0
        self.max_exponent = max_exponent

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_exponent is not None and self.exponent > self.max_exponent:
            raise StopIteration
        result = 2 ** self.exponent
        self.exponent += 1
        return result
