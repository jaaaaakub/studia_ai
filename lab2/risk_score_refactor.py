import pytest


def calculate_risk_score(age: int, cholesterol: int, max_heart_rate: int) -> float:
    """
    Oblicza uproszczony "wynik ryzyka” na podstawie trzech parametrów:

    age (wiek)
    cholesterol (poziom cholesterolu)
    max_heart_rate (maksymalne tętno)
    """
    
    if age < 0 or cholesterol < 0 or max_heart_rate <= 0:
        raise ValueError('All parameters must be positive.')

    score = age * 0.2 + cholesterol * 0.05 - max_heart_rate * 0.03
    return round(score, 2)


# =========================
# PARAMETRYZOWANE TESTY OK
# =========================
@pytest.mark.parametrize(
    "age, cholesterol, max_hr, expected",
    [
        (40, 200, 150, round(40 * 0.2 + 200 * 0.05 - 150 * 0.03, 2)),
        (0, 0, 1, round(0 + 0 - 1 * 0.03, 2)),
        (20, 100, 220, round(20 * 0.2 + 100 * 0.05 - 220 * 0.03, 2)),
    ],
)
def test_valid_inputs(age, cholesterol, max_hr, expected):
    assert calculate_risk_score(age, cholesterol, max_hr) == expected


# =========================
# TESTY WYJĄTKÓW
# =========================
@pytest.mark.parametrize(
    "age, cholesterol, max_hr",
    [
        (-1, 200, 150),
        (30, -10, 150),
        (30, 180, 0),
        (30, 180, -5),
    ],
)
def test_invalid_inputs(age, cholesterol, max_hr):
    with pytest.raises(ValueError):
        calculate_risk_score(age, cholesterol, max_hr)


# =========================
# EDGE CASES
# =========================
def test_large_values():
    result = calculate_risk_score(1000, 10000, 300)
    assert isinstance(result, float)


def test_rounding_precision():
    result = calculate_risk_score(33, 177, 123)
    assert round(result, 2) == result


# =========================
# RUNNER TESTÓW
# =========================
def run_all_tests():
    return pytest.main([__file__])

run_all_tests()
