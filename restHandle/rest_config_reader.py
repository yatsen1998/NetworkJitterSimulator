# -*- coding: utf-8 -*-
import json
import os
import sys

class restConfigReader:
    def __init__(self):
        self.cli_rest_config_path = '/usr/share/hcdserver/hcdcli/config.json'
        self.client_id = None
        self.client_secret = None
        self.grant_type = None
        self.username = None
        self.password = None
        self.mgmt_server_ip = None
        self.mgmt_server_port = None
        self.fetch_oauth_token = True

    def parse(self):
        if os.path.exists(self.cli_rest_config_path):
            json_data = json.load(open(self.cli_rest_config_path))
        else:
            sys.exit("ERROR: Cannot find HCLI config file!")

        self.client_id = json_data["clientId"]
        self.client_secret = json_data["clientSecret"]
        self.grant_type = json_data["grantType"]
        self.username = json_data["username"]
        self.password = json_data["password"]
        self.mgmt_server_ip = json_data["mgmtServerIp"]
        self.mgmt_server_port = json_data["mgmtServerPort"]
        if json_data["fetchOauthToken"] == 'false' or json_data["fetchOauthToken"] == 'False':
            self.fetch_oauth_token = False
            
