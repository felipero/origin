def test__consider_income_eq_zero(calculator, lines_score):
    profile_data = {
        "age": 45,
        "dependents": 2,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
    }

    calculator._RiskCalculator__consider_income(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": "ineligible",
        "home": 0,
        "life": 0,
    }


def test__consider_income_gt_200k(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": 2,
        "income": 200001,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
    }

    calculator._RiskCalculator__consider_income(lines_score, profile_data)
    assert lines_score == {
        "auto": -1,
        "disability": -1,
        "home": -1,
        "life": -1,
    }


def test__consider_income_between_0_and_200k(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": 2,
        "income": 100000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
    }

    calculator._RiskCalculator__consider_income(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }


def test__consider_income_inexistent(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": 2,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
    }

    calculator._RiskCalculator__consider_income(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": "ineligible",
        "home": 0,
        "life": 0,
    }
