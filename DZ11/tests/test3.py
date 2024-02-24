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
        (12.323, 1241.2131),
        (32.0, 12.0)
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
        (12.323, 1241.2131, '12.323/1241.2131'),
        (32.0, 12.0, '32.0/12.0')
    ]
)
def test_str(num, den, res):
    a = Fraction(num, den)
    assert str(a) == res


@pytest.mark.parametrize(
    ('values', 'ans'),
    [
        ('12 21', '12.0/21.0'),
        ('1141 2142', '1141.0/2142.0'),
        ('21.123 12.12', '21.123/12.12')
    ]
)
def test_input_digits(values, ans):
    a = Fraction()
    with mock.patch.object(builtins, 'input', lambda _: values):
        a.input_digits()

    assert str(a) == ans
