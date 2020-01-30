import datetime


def test__consider_vehicle_with_no_vehicle(calculator, lines_score):
    profile_data = {
        "age": 45,
        "dependents": 0,
        "income": 100,
        "risk_questions": [0, 0, 0],
    }

    calculator._RiskCalculator__consider_vehicle(lines_score, profile_data)
    assert lines_score == {
        "auto": "ineligible",
        "disability": 0,
        "home": 0,
        "life": 0,
    }


def test__consider_vehicle_with_year_older_than_5_years(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": 0,
        "income": 200,
        "risk_questions": [0, 0, 0],
        "vehicle": {"year": 2010},
    }

    calculator._RiskCalculator__consider_vehicle(lines_score, profile_data)
    assert lines_score == {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }


def test__consider_vehicle_with_year_in_the_last_5_years(calculator, lines_score):
    profile_data = {
        "age": 51,
        "dependents": 0,
        "income": 200,
        "risk_questions": [0, 0, 0],
        "vehicle": {"year": datetime.datetime.today().year - 4},
    }

    calculator._RiskCalculator__consider_vehicle(lines_score, profile_data)
    assert lines_score == {
        "auto": 1,
        "disability": 0,
        "home": 0,
        "life": 0,
    }
