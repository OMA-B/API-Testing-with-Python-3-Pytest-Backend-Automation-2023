from test_resources.src.utilities.db_utility import DBUtility
import random


class ProductsDAO(object):
    '''
    Access products present in the database
    '''
    def __init__(self) -> None:
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, quantity=1):

        sql_query = "SELECT * FROM local.wp_posts WHERE post_type = 'product' LIMIT 5000;"
        
        db_response = self.db_helper.execute_select(sql_query=sql_query)

        return random.sample(population=db_response, k=int(quantity)) 
