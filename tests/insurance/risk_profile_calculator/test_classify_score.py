def test__classify_score_with_score_eq_ineligible(calculator):
    assert calculator._RiskCalculator__classify_score("ineligible") == "ineligible"


def test__classify_score_with_score_lt_zero(calculator):
    assert calculator._RiskCalculator__classify_score(-1) == "economic"


def test__classify_score_with_score_eq_zero(calculator):
    assert calculator._RiskCalculator__classify_score(0) == "economic"


def test__classify_score_with_score_eq_1(calculator):
    assert calculator._RiskCalculator__classify_score(1) == "regular"


def test__classify_score_with_score_eq_2(calculator):
    assert calculator._RiskCalculator__classify_score(2) == "regular"


def test__classify_score_with_score_eq_3(calculator):
    assert calculator._RiskCalculator__classify_score(3) == "responsible"
