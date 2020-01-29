from insurance.services import RiskCalculator

calculator = RiskCalculator()


def test_calculate_score():

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


def test_calculate_score_with_age_eq_60():
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


def test_calculate_score_with_age_gt_60(client):
    profile_data = {
        "age": 61,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 100000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }

    response = client.post("/risk/profile/", profile_data, "application/json")
    risk_profile = {
        "auto": "regular",
        "disability": "ineligible",
        "home": "regular",
        "life": "ineligible",
    }
    assert calculator.calculate_score(profile_data) == risk_profile


def test_calculate_score_with_age_lt_30(client):
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


def test_calculate_score_with_no_income(client):
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


def test_calculate_score_with_no_house_nor_vehicle(client):
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
