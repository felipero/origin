def test__consider_house_mortage_eq_mortgaged(calculator, lines_score):
    profile_data = {
        "age": 45,
        "dependents": 0,
        "house": {"ownership_status": "mortgaged"},
        "income": 100,
        "risk_questions": [0, 0, 0],
    }

    calculator._RiskCalculator__consider_house_mortage(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 1,
        "home": 1,
        "life": 0,
    }


def test__consider_house_mortage_eq_owned(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": 0,
        "house": {"ownership_status": "owned"},
        "income": 200,
        "risk_questions": [0, 0, 0],
    }

    calculator._RiskCalculator__consider_house_mortage(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }


def test__consider_house_mortage_with_no_house(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": -2,
        "income": 10000,
        "risk_questions": [0, 0, 0],
    }

    calculator._RiskCalculator__consider_house_mortage(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 0,
        "home": "ineligible",
        "life": 0,
    }
