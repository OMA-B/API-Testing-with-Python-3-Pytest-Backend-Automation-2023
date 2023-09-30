import pytest

pytestmark = [pytest.mark.classic, pytest.mark.be]

@pytest.fixture(scope='module')
def my_setup():
    print('\n>>>> MY SETUP <<<<')

    return {'id': 10, 'name': 'OMA'}


@pytest.mark.classy
class TestWithClass(object):

    def test_active_login_user(self, my_setup):
        print('\nI am an actively logged in user')
        print('Yaaaaaaaaaaaaaay!!!!!')
        print(f'ID: {my_setup.get("id")}')


    def test_logged_out_user(self, my_setup):
        print('\nI am not a logged in user.')
        print('Sad face, duuuuuuuuuuuuuuuuuh!!!!')