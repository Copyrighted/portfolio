
def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated
    """
    assert new_user.email == 'testmail@gmail.com'
    assert new_user.password_hash != 'NotTheRightPassword'
    assert new_user.password_hash == '12345'
    assert new_user.is_authenticated()