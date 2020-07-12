import pytest
from webapp.models import User

@pytest.fixture(scope='module')
def new_user():
    # ID, e-mail, Password
    user = User()
    user.email = 'testmail@gmail.com'
    user.password_hash = '12345'
    return user
