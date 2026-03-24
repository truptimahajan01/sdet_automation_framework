def test_user_email(test_user):
    assert "@" in test_user["email"]

def test_user_password(test_user):
    assert len(test_user["password"]) >= 6