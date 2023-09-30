from test_resources.src.configs.hosts_config import API_HOSTS
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import requests, os, json, logging as logger

load_dotenv()

class RequestsMaker(object):

    def __init__(self) -> None:
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(client_key=os.getenv('WC_KEY'), client_secret=os.getenv('WC_SECRET'))

    def assert_status_code(self, expected_status_code):
        '''confirm if expected status code is returned.'''
        # import pdb; pdb.set_trace()
        assert self.response.status_code == expected_status_code, f'Bad Status Code. Expected: {expected_status_code}, but Actual Status Code: {self.response.status_code}, URL: {self.url}, Response Json: {self.response.json()}'

    
    def make_requests(self, endpoint, method, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {'Content-Type': 'application/json'}

        self.url = self.base_url + endpoint

        if method == 'post':
            self.response = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        else:
            self.response = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)

        
        # verify status code of the call
        self.assert_status_code(expected_status_code)

        return self.response.json()


    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        '''make POST request to the API'''
        method = 'post'

        request_json_response = self.make_requests(endpoint=endpoint, method=method, payload=payload, headers=headers, expected_status_code=expected_status_code)

        logger.debug(f'POST API Response: {request_json_response}')

        return request_json_response
    
    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        '''make GET request to the API'''
        method = 'get'

        request_json_response = self.make_requests(endpoint=endpoint, method=method, payload=payload, headers=headers, expected_status_code=expected_status_code)

        logger.debug(f'GET API Response: {request_json_response}')

        return request_json_response