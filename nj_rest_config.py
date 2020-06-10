# -*- coding: utf-8 -*-

import os
import json
import sys

# from log_loader import LogInit

# log = LogInit()


class NetworkJitterRestConfig:
    def __init__(self):
        self.nj_rest_config_path = '/scratch/network_jitter_test/config.json'
        self.client_id = None
        self.client_secret = None
        self.grant_type = None
        self.username = None
        self.password = None
        self.mgmt_server_ip = None
        self.mgmt_server_port = None
        self.fetch_oauth_token = True
        
        
    def parse(self):
        """
        Parse config.json file to fetch REST config parameters.

        """
        if os.path.exists(self.nj_rest_config_path):
            json_data = json.load(open(self.nj_rest_config_path))
        else:
            sys.exit("ERROR: Cannot find NetworkJitter config file!")

        self.client_id = json_data["client_id"]
        self.client_secret = json_data["client_secret"]
        self.grant_type = json_data["grant_type"]
        self.username = json_data["web_ui_username"]
        self.password = json_data["web_ui_password"]
        self.mgmt_server_ip = json_data["mgmt_server_ip"]
        self.mgmt_server_port = json_data["mgmt_server_port"]
        if json_data["fetchOauthToken"] == 'false' or json_data["fetchOauthToken"] == 'False':
            self.fetch_oauth_token = False
        