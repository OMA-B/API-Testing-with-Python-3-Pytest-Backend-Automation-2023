from test_resources.src.utilities.request_utility import RequestsMaker


class ProductsHelper(object):
    '''
    Make API calls for products
    '''

    def __init__(self) -> None:
        self.request_maker = RequestsMaker()

    
    def get_product_by_id(self, product_id):

        return self.request_maker.get(endpoint=f'products/{product_id}')

    
    def create_product(self, payload):
        return self.request_maker.post(endpoint='products', payload=payload, expected_status_code=201)