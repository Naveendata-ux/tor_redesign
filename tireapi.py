from __future__ import print_function
import time
import ws_api_client
from ws_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: user_key
ws_api_client.configuration.default_config.api_key['user_key'] = '4a7488fedfd6685e3ba26c495bf569c9'
# create an instance of the API class
api_instance = ws_api_client.MakesApi()
#countries = 'us,gb,jp' # str | Show information for local manufacturers from specified countries only. Use `GET /countries/` method to get the full list of countries. (e.g. `us,gb,jp`) (optional)
countries = 'us,ca'
try:
    # Get list of manufacturers
    api_response = api_instance.makes_list(countries=countries)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MakesApi->makes_list: %s\n" % e)
