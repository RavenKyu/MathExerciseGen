import random
from fractions import Fraction

# random.seed(1)

numerator = random.randint(1, 100)
denominator = random.randint(1, 100)

print(Fraction(numerator, denominator))



