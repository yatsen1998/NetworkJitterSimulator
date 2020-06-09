# -*- coding: utf-8 -*-

import requests
from log_loader import logInit

log = logInit()

REST_API_VERSION = 1


class OauthClient:
    def __init__(self,api_version=REST_API_VERSION, *args, **kwargs):
        self.access_token = None
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.client_id = kwargs['client_id']
        self.client_secret = kwargs['client_secret']
        self.verify = kwargs['verify']
        self.mvip=kwargs['mvip']
        self.mgmt_server_port=8443
        self.base_endpoint= 'https://{}:{}'.format(self.mvip,self.mgmt_server_port)
        self.access_token_endpoint=self.base_endpoint+'/ouath/token'
 
        
        
    def get_access_token(self):
        response = requests.post(self.access_token_endpoint,
                                 verify=self.verify,
                                 auth=(self.client_id, self.client_secret),
                                 data={'grant_type': 'password', 'username': self.username,
                                       'password': self.password}
                                 )
        if response.status_code != 200:
            log.logger.info("Failed to login for user {}".format(self.username))
        self.access_token = response.json()['access_token']
        self.headers = {'authorization': 'Bearer {}'.format(self.access_token)}
        
        
tg = OauthClient(REST_API_VERSION,)