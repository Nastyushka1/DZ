class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator, self.denominator = self.validate(numerator, denominator)

    def input_fraction(self):
        self.numerator, self.denominator = self.validate(*input("Введите числитель и знаменатель через пробел: ").split(' '))

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    @staticmethod
    def validate(num, den):
        if den == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю")
        if str(num).isdigit() and str(den).isdigit():
            return int(num), int(den)
        raise ValueError('Неверный формат данных')


f = Fraction(12, 13)
f.validate(12, 1)
f.input_fraction()
print(type(f.numerator))
