def test_calculate_score(calculator):

    profile_data = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }

    risk_profile = {
        "auto": "regular",
        "disability": "ineligible",
        "home": "economic",
        "life": "regular",
    }
    assert calculator.calculate_score(profile_data) == risk_profile


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

    risk_profile = {
        "auto": "regular",
        "disability": "responsible",
        "home": "regular",
        "life": "responsible",
    }
    assert calculator.calculate_score(profile_data) == risk_profile


def test_calculate_score_with_age_gt_60(calculator):
    profile_data = {
        "age": 61,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 100000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }

    risk_profile = {
        "auto": "regular",
        "disability": "ineligible",
        "home": "regular",
        "life": "ineligible",
    }
    assert calculator.calculate_score(profile_data) == risk_profile


def test_calculate_score_with_age_lt_30(calculator):
    profile_data = {
        "age": 28,
        "dependents": 0,
        "house": {"ownership_status": "owned"},
        "income": 100000,
        "marital_status": "single",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }

    risk_profile = {
        "auto": "economic",
        "disability": "economic",
        "home": "economic",
        "life": "economic",
    }
    assert calculator.calculate_score(profile_data) == risk_profile


def test_calculate_score_with_no_income(calculator):
    profile_data = {
        "age": 28,
        "dependents": 0,
        "house": {"ownership_status": "owned"},
        "marital_status": "single",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }

    risk_profile = {
        "auto": "economic",
        "disability": "ineligible",
        "home": "economic",
        "life": "economic",
    }

    assert calculator.calculate_score(profile_data) == risk_profile


def test_calculate_score_with_no_house_nor_vehicle(calculator):
    profile_data = {
        "age": 31,
        "dependents": 2,
        "income": 100000,
        "marital_status": "single",
        "risk_questions": [0, 1, 0],
    }

    risk_profile = {
        "auto": "ineligible",
        "disability": "regular",
        "home": "ineligible",
        "life": "regular",
    }

    assert calculator.calculate_score(profile_data) == risk_profile
