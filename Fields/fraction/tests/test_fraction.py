from unittest import TestCase
from Fields.fraction import Fraction

class Test(TestCase):
    def setUp(self):
        self.fract = Fraction(seed=3)

    def test_pattern_fraction_lv0020(self):
        tex, answer, desc = self.fract.pattern_fraction_lv0020()
        print(tex, answer, desc)
