import pytest, pdb


pytestmark = pytest.mark.functional

@pytest.fixture(scope='module')
def my_setup():
    print('\n>>>> MY SETUP <<<<')

    return {'id': 10, 'name': 'OMA'}

@pytest.mark.first
def test_active_login_user(my_setup):
    print('\nI am an actively logged in user')
    print('Yaaaaaaaaaaaaaay!!!!!')
    # pdb.set_trace()
    print(f'Username: {my_setup["name"]}')

@pytest.mark.second
def test_logged_out_user(my_setup):
    print('\nI am not a logged in user.')
    print('Sad face, duuuuuuuuuuuuuuuuuh!!!!')
    # assert 1 == 0, 'not signed in!'