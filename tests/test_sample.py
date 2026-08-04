import pytest
from utils.data_reader import read_csv


@pytest.mark.parametrize("credentials", read_csv("data.csv"))
def test_csv_credentials_have_valid_email(credentials):
    """Verify test data CSV contains properly formatted email addresses."""
    assert "@" in credentials["email"]
    assert "." in credentials["email"]


@pytest.mark.parametrize("credentials", read_csv("data.csv"))
def test_csv_credentials_have_password(credentials):
    """Verify test data CSV contains non-empty passwords."""
    assert len(credentials["password"]) >= 6