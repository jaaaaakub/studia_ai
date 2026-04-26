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


def test_basic_case():
    result = calculate_risk_score(40, 200, 150)
    expected = round(40 * 0.2 + 200 * 0.05 - 150 * 0.03, 2)
    assert result == expected


def test_min_values():
    result = calculate_risk_score(0, 0, 1)
    expected = round(0 + 0 - 1 * 0.03, 2)
    assert result == expected


def test_negative_age():
    with pytest.raises(ValueError):
        calculate_risk_score(-1, 200, 150)


def test_negative_cholesterol():
    with pytest.raises(ValueError):
        calculate_risk_score(30, -10, 150)


def test_zero_heart_rate():
    with pytest.raises(ValueError):
        calculate_risk_score(30, 180, 0)


def test_negative_heart_rate():
    with pytest.raises(ValueError):
        calculate_risk_score(30, 180, -5)


def test_negative_score():
    result = calculate_risk_score(20, 100, 220)
    assert result < 0


def test_large_values():
    result = calculate_risk_score(1000, 10000, 300)
    assert isinstance(result, float)


def test_rounding():
    result = calculate_risk_score(33, 177, 123)
    assert round(result, 2) == result  # upewniamy się, że wynik jest zaokrąglony
