import pytest

from calculator.core import calc


@pytest.mark.parametrize("test_input, expected", [
    ("1+1", "2"),
    ("3-1", "2"),
    ("2*2", "4"),
    ("6/2", "3"),
])
def test_calc_natural(test_input, expected):
    assert calc(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    ("-2+1", "-1"),
    ("3-5", "-2"),
    ("-1*9", "-9"),
    ("-3/3", "-1")
])
def test_calc_integer(test_input, expected):
    assert calc(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    ("0.1", "0.1"),
    ("0.1+0.1", "0.2")
])
def test_calc_float(test_input, expected):
    assert calc(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    ("3/9", "1/3 ≈ 0.3333333333333333"),
    ("5/25", "1/5 = 0.2")
])
def test_calc_rational(test_input, expected):
    assert calc(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    ("pi", "π ≈ 3.141592653589793"),
    ("3pi", "3⋅π ≈ 9.42477796076938"),
    ("3⋅π", "3⋅π ≈ 9.42477796076938"),
    ("sqrt(2)", "√2 ≈ 1.4142135623730951"),
    ("√2", "√2 ≈ 1.4142135623730951"),
    ("φ", "φ ≈ 1.618033988749895")
])
def test_calc_real(test_input, expected):
    assert calc(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    ("1 + i", "1 + ⅈ"),
    ("3*i", "3⋅ⅈ"),
    ("1/3+i", "1/3 + ⅈ ≈ 0.3333333333333333 + ⅈ"),
    ("1/5+i", "1/5 + ⅈ = 0.2 + ⅈ"),
    ("1+(1/3)*i", "    ⅈ\n1 + ─\n    3 ≈ 1 + 0.3333333333333333⋅ⅈ"),
    ("1/5+3i", "1/5 + 3⋅ⅈ = 0.2 + 3⋅ⅈ"),
    ("π*ⅈ", "ⅈ⋅π ≈ 3.141592653589793⋅ⅈ")
])
def test_calc_complex(test_input, expected):
    assert calc(test_input, latex=False) == expected


@pytest.mark.parametrize("test_input, expected", [
    ("oo", "∞"),
    ("zoo", "zoo")
])
def test_calc_edge_case(test_input, expected):
    assert calc(test_input, latex=False) == expected


@pytest.mark.parametrize("test_input, expected", [
    ("θ(9)", "1"),
    ("θ(-9)", "0"),
    # ("θ(0)", "1"),
    ("sin(pi)", "0"),
    ("cos(pi)", "-1"),
    ("tan(pi)", "0"),
    ("cos 0", "1"),
    # ("sin(90°)", "1"),
    # ("cos(90°)", "0")
])
def test_calc_function(test_input, expected):
    assert calc(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    ("3x=5", "{5/3}")
])
def test_calc_equation(test_input, expected):
    assert calc(test_input, latex=False) == expected
