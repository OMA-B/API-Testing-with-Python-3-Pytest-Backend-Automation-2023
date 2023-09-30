from woocommerce import API
import pprint

wcapi = API(
    url="http://localhost:10004/",
    consumer_key="ck_3eaf977bb59ecb5e4dc0d6ecae4bb544902aa49a",
    consumer_secret="cs_33fbbe0a05fa86080fcd25d552806d99b2a72606",
    version="wc/v3"
)

r = wcapi.get("orders")
pprint.pprint(r.json())
