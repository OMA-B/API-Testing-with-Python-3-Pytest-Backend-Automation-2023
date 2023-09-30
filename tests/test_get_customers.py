import pytest, logging as logger
from test_resources.src.utilities.request_utility import RequestsMaker



@pytest.mark.customers
@pytest.mark.tcid30
def test_get_customers():
    logger.debug('Fetching call created customers info.')

    request_maker = RequestsMaker()
    customers_info = request_maker.get(endpoint='customers')

    assert len(customers_info) > 0, 'No customer data was returned. Perhaps, consider creating customers first.'

