# -*- coding: utf-8 -*-
import requests.adapters
import urllibs3

from rest_config_reader import restConfigReader

config = restConfigReader()
config.parse()
client_secret = config.client_secret
client_id = config.client_id
grant_type = config.grant_type
username = config.username
password = config.password
mgmt_server_ip = config.mgmt_server_ip
mgmt_server_port = config.mgmt_server_port

base_endpoint = 'https://{}:{}'.format(mgmt_server_ip, mgmt_server_port)
access_token_endpoint = base_endpoint + '/oauth/token'
session_ = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10)
session_.mount('https://', adapter)

if config.fetch_oauth_token:
    response = session_.post(access_token_endpoint,
                             verify=False,
                             auth=(client_id, client_secret),
                             data={'grant_type': grant_type, 'username': username,
                                   'password': password}
                             )

    if response.status_code == 200:
        json_response_dict = response.json()
        access_token = json_response_dict.get('access_token')
        header = {'authorization': 'Bearer {}'.format(access_token)}
    else:
        raise Exception('Failed to get an access token - Please check if all the fields in the hcli config.json file '
                        'is correct!')
        
        