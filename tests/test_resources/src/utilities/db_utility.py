import pymysql, os
from dotenv import load_dotenv

load_dotenv()



class DBUtility(object):
    '''connecting to database and executing commands'''

    def __init__(self) -> None:
        pass

    def create_connection(self):
        connection = pymysql.connect(host='localhost', user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), port=10010)

        return connection

    def execute_select(self, sql_query):
        db_connect = self.create_connection()

        try:
            cursor = db_connect.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql_query)
            dict_response = cursor.fetchall()
            cursor.close()
        except Exception as e:
            raise Exception(f'Failed to run the query: {sql_query}\nError: {e}')
        else:
            return dict_response
        finally:
            db_connect.close()

    def execute_sql(self, sql_query):
        pass
