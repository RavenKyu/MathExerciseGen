import random

class Base:
    def __init__(self, seed):
        random.seed(seed)

    @staticmethod
    def get_random_int():
        return random.randint()

    @staticmethod
    def get_random_ranged_int(a: int, b: int):
        return random.randint(a, b)

    def patterns(self):
        raise NotImplemented