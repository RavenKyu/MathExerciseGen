from unittest import TestCase
from Fields.fraction import Fraction
from documents import Document

class Test(TestCase):
    def setUp(self):
        import time
        self.document = Document()
        self.fract = Fraction(seed=time.time())

    def test_gerenate(self):
        questions = list()
        for _ in range(0, 10):
            questions.append(self.fract.pattern_fraction_lv0020())
        ex = {'description': '분수끼리의 덧셈 (초5 1학기)',
              'pattern': questions}
        self.document.add_exercise(ex)

        questions = list()
        for _ in range(0, 10):
            questions.append(self.fract.pattern_fraction_lv0030())
        ex = {'description': '분수끼리의 뺄셈 (초5 1학기)',
              'pattern': questions}
        self.document.add_exercise(ex)

        questions = list()
        for _ in range(0, 10):
            questions.append(self.fract.pattern_fraction_lv0040())
        ex = {'description': '분수끼리의 곱셈 (초5 2학기)',
              'pattern': questions}
        self.document.add_exercise(ex)

        questions = list()
        for _ in range(0, 10):
            questions.append(self.fract.pattern_fraction_lv0050())
        ex = {'description':'분수끼리의 나눗셈 (초5 2학기)',
              'pattern':questions}
        self.document.add_exercise(ex)

        print(self.document.generate_tex())