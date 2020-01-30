from insurance.services import RiskCalculator
import pytest


@pytest.fixture
def lines_score():
    return {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }


@pytest.fixture(scope="session")
def calculator():
    return RiskCalculator()
