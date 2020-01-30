def test__consider_dependents_eq_zero(calculator, lines_score):
    profile_data = {
        "age": 45,
        "dependents": 0,
        "income": 100,
        "marital_status": "married",
        "risk_questions": [0, 0, 0],
    }

    calculator._RiskCalculator__consider_dependents(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }


def test__consider_dependents_gt_0(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": 1,
        "income": 200,
        "marital_status": "married",
        "risk_questions": [0, 0, 0],
    }

    calculator._RiskCalculator__consider_dependents(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 1,
        "home": 0,
        "life": 1,
    }


def test__consider_dependents_negative(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": -2,
        "income": 10000,
        "marital_status": "married",
        "risk_questions": [0, 0, 0],
    }

    calculator._RiskCalculator__consider_dependents(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }


def test__consider_dependents_inexistent(calculator, lines_score):
    profile_data = {
        "age": 51,
        "income": 10000,
        "marital_status": "married",
        "risk_questions": [0, 0, 0],
    }

    calculator._RiskCalculator__consider_dependents(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }
