def test__consider_senior_age_with_age_eq_60(calculator, lines_score):
    profile_data = {
        "age": 60,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 100000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }

    calculator._RiskCalculator__consider_senior_age(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }


def test__consider_senior_age_with_age_gt_60(calculator, lines_score):
    profile_data = {
        "age": 61,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 100000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }

    calculator._RiskCalculator__consider_senior_age(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": "ineligible",
        "home": 0,
        "life": "ineligible",
    }


def test__consider_senior_age_with_age_lt_60(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 100000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }

    calculator._RiskCalculator__consider_senior_age(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }
