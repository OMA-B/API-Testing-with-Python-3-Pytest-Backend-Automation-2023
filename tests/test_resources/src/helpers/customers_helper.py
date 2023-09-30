from test_resources.src.utilities.generic_utilities import generate_random_email_and_password
from test_resources.src.utilities.request_utility import RequestsMaker


class CustomersHelper(object):
    '''
    Make API calls for customers
    '''

    def __init__(self) -> None:
        self.request_maker = RequestsMaker()

    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            random_info = generate_random_email_and_password()
            email = random_info['email']
        if not password:
            password = 'Password1'

        payload = {'email': email, 'password': password}
        payload.update(kwargs)

        created_customer_json = self.request_maker.post(endpoint='customers', payload=payload, expected_status_code=201)

        return created_customer_json