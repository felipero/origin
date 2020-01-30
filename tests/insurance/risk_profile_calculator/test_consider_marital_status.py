def test__consider_marital_status_eq_married(calculator, lines_score):
    profile_data = {
        "age": 45,
        "dependents": 0,
        "income": 100,
        "marital_status": "married",
        "risk_questions": [0, 0, 0],
    }

    calculator._RiskCalculator__consider_marital_status(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 1,
        "home": 0,
        "life": 1,
    }


def test__consider_marital_status_eq_single(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": 0,
        "income": 200,
        "marital_status": "single",
        "risk_questions": [0, 0, 0],
    }

    calculator._RiskCalculator__consider_marital_status(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }


def test__consider_marital_status_inexisting(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": -2,
        "income": 10000,
        "risk_questions": [0, 0, 0],
    }

    calculator._RiskCalculator__consider_marital_status(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }
