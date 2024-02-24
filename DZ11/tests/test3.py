import pytest
import mock
import builtins
from v0 import Fraction


@pytest.mark.parametrize(
    ('num', 'den'),
    [
        (12, 12),
        (23, 121),
        (0, 1),
    ]
)
def test_init(num, den):
    a = Fraction(num, den)
    assert a.numerator == num
    assert a.denominator == den


@pytest.mark.parametrize(
    ('num', 'den', 'res'),
    [
        (12, 12, '12/12'),
        (23, 121, '23/121'),
        (0, 1, '0/1'),
    ]
)
def test_str(num, den, res):
    a = Fraction(num, den)
    assert str(a) == res


@pytest.mark.parametrize(
    ('values', 'ans'),
    [
        ('12 21', '12/21'),
        ('1141 2142', '1141/2142'),
        ('0 1', '0/1')
    ]
)
def test_input_digits(values, ans):
    a = Fraction()
    with mock.patch.object(builtins, 'input', lambda _: values):
        a.input_fraction()
    assert str(a) == ans


@pytest.mark.parametrize(
    ('num', 'den', 'res'),
    [
        ('12', '15', (12, 15)),
        (1, 12, (1, 12)),
        ('12232', '213', (12232, 213))
    ]
)
def test_validity(num, den, res):
    a = Fraction()
    assert a.validate(num, den) == res


def test_validity_exception():
    a = Fraction()
    with pytest.raises(ZeroDivisionError, match="Знаменатель не может быть равен нулю"):
        a.validate(1, 0)
    with pytest.raises(ValueError, match='Неверный формат данных'):
        a.validate('ewfmlkwje', 'kl;afsnar')
