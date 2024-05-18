from __future__ import print_function


from pprint import pprint

import cloudmersive_virus_api_client

from cloudmersive_virus_api_client.rest import ApiException


configuration = cloudmersive_virus_api_client.Configuration()
configuration.api_key['Apikey'] = '6f8b9a59-4de0-47d9-9e51-08a69b24aaeb'


api_instance = cloudmersive_virus_api_client.ScanApi(cloudmersive_virus_api_client.ApiClient(configuration))


def scan(input_file='EICAR TEST FILE.txt'):
    try:

        api_response = api_instance.scan_file(input_file)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ScanApi->scan_file: %s\n" % e)
