def test_risk_profile_with_valid_payload(client):

    payload = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }

    response = client.post("/risk/profile/", payload, "application/json")
    risk_profile_json = '{"auto":"regular","disability":"ineligible","home":"economic","life":"regular"}'
    assert response.content.decode() == risk_profile_json
    assert response.status_code == 200
