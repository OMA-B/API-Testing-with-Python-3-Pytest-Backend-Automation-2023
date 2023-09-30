import logging as logger, pytest
from test_resources.src.utilities.generic_utilities import generate_random_name
from test_resources.src.helpers.products_helper import ProductsHelper


@pytest.mark.tcid26
def test_create_a_simple_product():

    logger.debug('Creating a single simple product in Store.')    
    # create payload
    random_name = generate_random_name(length=20)
    payload = {'name': random_name, 'type': 'simple', 'regular_price': 10.99}
    
    # make the call
    created_product = ProductsHelper().create_product(payload=payload)

    import pdb; pdb.set_trace()

    # verify the response

    # verify product is created in the database
