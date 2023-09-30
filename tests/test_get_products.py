import pytest, logging as logger
from test_resources.src.utilities.request_utility import RequestsMaker
from test_resources.src.DAO.products_dao import ProductsDAO
from test_resources.src.helpers.products_helper import ProductsHelper



@pytest.mark.tcid24
def test_get_all_products():
    logger.debug('Fetching all products in Store...')

    # make the call
    request_maker = RequestsMaker()
    all_products = request_maker.get(endpoint='products', payload={'per_page': 100})
    # verify the response
    assert len(all_products) > 0, 'No product data returned. Perhaps, consider creating some products.'


@pytest.mark.tcid25
def test_get_product_by_id():

    # get random product from db
    db_call = ProductsDAO()
    random_product = db_call.get_random_product_from_db(quantity=1)
    db_product_id = random_product[0]['ID']
    db_product_name = random_product[0]['post_title']

    # make the call
    product_helper = ProductsHelper()
    requested_product = product_helper.get_product_by_id(product_id=db_product_id)
    api_product_id = requested_product['id']
    api_product_name = requested_product['name']
    
    # verify the response
    assert db_product_name == api_product_name, f'Different product got returned from API. Expected: {db_product_name} with ID {db_product_id}, Actual: {api_product_name} with ID {api_product_id}'
    