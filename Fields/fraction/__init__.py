import fractions
from Fields import Base


class Frac(fractions.Fraction):
    @property
    def tex(self):
        tex = list()
        if self.denominator == self.numerator:
            tex.append('1')
        f = '\\frac{n.numerator}' \
            '{n.denominator}'.replace('{', '{{{').replace('}', '}}}')
        tex.append(f.format(n=self))
        return tex

class Fraction(Base):
    def get_random_fraction(self, *_range):
        if not _range:
            _range = (2, 100)
        numerator = self.get_random_ranged_int(*_range)
        denominator = self.get_random_ranged_int(*_range)
        return Frac(numerator, denominator)

    def pattern_fraction_lv0020(self):
        question = '분수끼리의 덧셈'
        # \frac{3}{4}+\frac{4}{5}
        # 공통 분모로 만들어준다.
        # 분모가 같은 분자끼리 묶는다.
        f1 = self.get_random_fraction(2, 10)
        f2 = self.get_random_fraction(2, 10)

        tex = '\\frac{n1.numerator}{d1.denominator}+\\frac{n2.numerator}{d2.denominator}'.replace(
            '{', '{{{').replace('}', '}}}')
        tex = tex.format(n1=f1, d1=f1, n2=f2, d2=f2)

        af = f1 + f2
        answer = '\\frac{af.numerator}{af.denominator}'.replace(
            '{', '{{{').replace('}', '}}}')
        answer = answer.format(af=af)
        return tex, answer

    def pattern_fraction_lv0030(self):
        question = '분수끼리의 뺄셈'
        # \frac{3}{4}-\frac{4}{5}
        # 공통 분모로 만들어준다.
        # 분모가 같은 분자끼리 묶는다.
        f1 = self.get_random_fraction(2, 10)
        f2 = self.get_random_fraction(2, 10)

        tex = '\\frac{n1.numerator}{d1.denominator}-\\frac{n2.numerator}{' \
              'd2.denominator}'.replace('{', '{{{').replace('}', '}}}')
        tex = tex.format(n1=f1, d1=f1, n2=f2, d2=f2)

        af = f1 - f2
        answer = '\\frac{af.numerator}{af.denominator}'.replace(
            '{', '{{{').replace('}', '}}}')
        answer = answer.format(af=af)
        return tex, answer

    def pattern_fraction_lv0040(self):
        question = '분수끼리의 곱셈'
        # \frac{3}{4}-\frac{4}{5}
        # 공통 분모로 만들어준다.
        # 분모가 같은 분자끼리 묶는다.
        f1 = self.get_random_fraction(2, 10)
        f2 = self.get_random_fraction(2, 10)

        tex = '\\frac{n1.numerator}{d1.denominator} \\times \\frac{' \
              'n2.numerator}{' \
              'd2.denominator}'.replace('{', '{{{').replace('}', '}}}')
        tex = tex.format(n1=f1, d1=f1, n2=f2, d2=f2)

        af = f1 * f2
        answer = '\\frac{af.numerator}{af.denominator}'.replace(
            '{', '{{{').replace('}', '}}}')
        answer = answer.format(af=af)
        return tex, answer

    def pattern_fraction_lv0050(self):
        question = '분수끼리의 나눗셈'
        # \frac{3}{4}-\frac{4}{5}
        # 공통 분모로 만들어준다.
        # 분모가 같은 분자끼리 묶는다.
        f1 = self.get_random_fraction(2, 10)
        f2 = self.get_random_fraction(2, 10)

        tex = '\\frac{n1.numerator}{d1.denominator} \\div  \\frac{' \
              'n2.numerator}{' \
              'd2.denominator}'.replace('{', '{{{').replace('}', '}}}')
        tex = tex.format(n1=f1, d1=f1, n2=f2, d2=f2)

        af = f1 / f2
        answer = '\\frac{af.numerator}{af.denominator}'.replace(
            '{', '{{{').replace('}', '}}}')
        answer = answer.format(af=af)
        return tex, answer