import pytest, logging as logger
from test_resources.src.utilities.generic_utilities import generate_random_email_and_password
from test_resources.src.utilities.request_utility import RequestsMaker
from test_resources.src.helpers.customers_helper import CustomersHelper
from test_resources.src.DAO.customers_dao import CustomersDAO


@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_by_email_and_password():

    logger.info("TEST: Create customer email and password only.")

    # create payload
    random_info = generate_random_email_and_password()
    email = random_info['email']
    password = random_info['password']

    # make the call
    customer_object = CustomersHelper()
    customer_info = customer_object.create_customer(email=email, password=password)
    
    # verify email in the response
    assert customer_info['email'] == email, f"Create customer API returned wrong email. Email expected: {email}, Returned: {customer_info['email']}"
    assert customer_info['first_name'] == '', f'Create customer API returned value for first_name, but it should be empty. Value returned: {customer_info["first_name"]}'

    # verify customer is created in the database
    customer_dao = CustomersDAO()
    query_response = customer_dao.get_customer_by_email(email=email)

    id_in_api_response = customer_info['id']
    id_in_db_response = query_response[0]['ID']

    assert id_in_api_response == id_in_db_response, f'Customer created id in API - {id_in_api_response} - is not the same with ID - {id_in_db_response} - returned from database. Email: {email}'


@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    
    # get existing email from db
    customer_db = CustomersDAO()
    existing_customer = customer_db.get_random_customer_from_db()
    existing_customer_email = existing_customer[0]['user_email']

    # make the call
    request_maker = RequestsMaker()
    payload = {'email': existing_customer_email, 'password': 'Password1'}
    customer_info = request_maker.post(endpoint='customers', payload=payload, expected_status_code=400)

    assert customer_info["code"] == 'registration-error-email-exists', f'Create customer with existing email error code not correct. Expected: "registration-error-email-exists", Actual: {customer_info["code"]}'