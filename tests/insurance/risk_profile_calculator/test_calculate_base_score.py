def test__calculate_base_score_with_no_special_age(calculator):
    profile_data = {
        "age": 41,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [1, 1, 1],
        "vehicle": {"year": 2018},
    }

    assert calculator._RiskCalculator__calculate_base_score(profile_data) == 3


def test__calculate_base_score_with_age_under_30(calculator):
    profile_data = {
        "age": 21,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 200001,
        "marital_status": "married",
        "risk_questions": [0, 0, 0],
        "vehicle": {"year": 2018},
    }

    assert calculator._RiskCalculator__calculate_base_score(profile_data) == -2


def test__calculate_base_score_with_age_between_30_and_40(calculator):
    profile_data = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 100000,
        "marital_status": "married",
        "risk_questions": [0, 0, 0],
        "vehicle": {"year": 2018},
    }

    assert calculator._RiskCalculator__calculate_base_score(profile_data) == -1


def test__calculate_base_score_with_age_eq_40(calculator):
    profile_data = {
        "age": 40,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 100000,
        "marital_status": "married",
        "risk_questions": [0, 0, 0],
        "vehicle": {"year": 2018},
    }

    assert calculator._RiskCalculator__calculate_base_score(profile_data) == -1


def test__calculate_base_score_with_age_eq_30(calculator):
    profile_data = {
        "age": 40,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 100000,
        "marital_status": "married",
        "risk_questions": [0, 0, 0],
        "vehicle": {"year": 2018},
    }

    assert calculator._RiskCalculator__calculate_base_score(profile_data) == -1


def test__calculate_base_score_with_negative_risk_questions(calculator):
    profile_data = {
        "age": 45,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 100000,
        "marital_status": "married",
        "risk_questions": [-1, -1, -1],
        "vehicle": {"year": 2018},
    }

    assert calculator._RiskCalculator__calculate_base_score(profile_data) == -3
