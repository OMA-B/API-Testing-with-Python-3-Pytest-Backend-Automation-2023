from test_resources.src.utilities.db_utility import DBUtility
import logging as logger, random


class CustomersDAO(object):
    '''connect to database and query customer data from it'''
    
    def __init__(self) -> None:
        self.db_helper = DBUtility()


    def get_customer_by_email(self, email):

        select_query = f'SELECT * FROM local.wp_users WHERE user_email = "{email}";'

        select_query_response = self.db_helper.execute_select(sql_query=select_query)

        logger.debug(f'Query Response: {select_query_response}, gotten from the query: {select_query}')

        return select_query_response

    
    def get_random_customer_from_db(self, quantity=1):

        sql_query = 'SELECT * FROM local.wp_users ORDER BY id DESC LIMIT 5000;'

        sql_query_response = self.db_helper.execute_select(sql_query=sql_query)

        return random.sample(population=sql_query_response, k=int(quantity))
        