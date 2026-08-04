def test_user_email_has_at_symbol(test_user):
    """Email in test_user fixture should contain '@'."""
    assert "@" in test_user["email"]


def test_user_password_meets_min_length(test_user):
    """Password in test_user fixture should be at least 8 characters."""
    assert len(test_user["password"]) >= 8