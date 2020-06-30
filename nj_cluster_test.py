# -*- coding: utf-8 -*-

import utils
import urllib3
import requests
from prettytable import PrettyTable

from log_loader import LogInit
from rest_handler import RestHandler

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

log = LogInit()



class NJClusterTester:
    """
        Designed to check whether cluster information can be fetched under various network conditions
        Not functional right now.
    
    """    
    def __init__(self):
        self.rest_handler = RestHandler()
        self.clusters_endpoint = self.rest_handler.base_endpoint + '/v1/clusters'
        
    def check_cluster_info(self, cluster_id=None):
        if not cluster_id:
            response = requests.get(self.clusters_endpoint,
                                    verify=False,
                                    headers=self.rest_handler.header
                                    )
            json_response_dict = response.json()
            if response.status_code == 200:
                t = PrettyTable(['Cluster ID', 'Cluster Name', 'Type', 'Access Level', 'Created Time', 'Updated Time',
                                 'Minimum Cluster Size', 'Replication Factor', 'Block Size', 'State', 'Health State',
                                 'Total Space', 'Used Space', 'Virtual IP'])
                for cluster_bean in json_response_dict.values()[0]:
                    cluster_id = cluster_bean.get('clusterId')
                    cluster_name = cluster_bean.get('clusterName')
                    cluster_type = cluster_bean.get('type')
                    access_level = cluster_bean.get('clusterAccessLevel')
                    created_time = utils.get_datetime_from_epoch(cluster_bean.get('clusterCreateTime'))
                    updated_time = utils.get_datetime_from_epoch(cluster_bean.get('clusterUpdateTime'))
                    min_cluster_size = cluster_bean.get('minClusterSize')
                    replication_factor = cluster_bean.get('replicationFactor')
                    block_size = cluster_bean.get('blockSize')
                    total_space = utils.get_human_readable_size(cluster_bean.get('usableSpace'))
                    used_space = utils.get_human_readable_size(cluster_bean.get('usedSpace'))
                    virtual_ip = cluster_bean.get('virtualIp')
                    cluster_state = cluster_bean.get('state')
                    cluster_health_state = cluster_bean.get('healthState')

                    t.add_row([cluster_id, cluster_name, cluster_type, access_level, created_time, updated_time,
                               min_cluster_size, replication_factor, block_size, cluster_state, cluster_health_state,
                               total_space, used_space, virtual_ip])
                print (t)
                return json_response_dict.values()[0]
            else:
                log.logger.exception(json_response_dict)
                raise Exception('Failed to get all clusters')
        else:
            get_cluster_by_id_endpoint = self.clusters_endpoint + '/{}'.format(cluster_id)
            response = requests.get(get_cluster_by_id_endpoint,
                                    verify=False,
                                    headers=self.rest_handler.header
                                    )
            json_response_dict = response.json()
            if response.status_code == 200:
                t = PrettyTable(['Cluster Name', 'Type', 'Access Level', 'Created Time', 'Updated Time',
                                 'Minimum Cluster Size', 'Replication Factor', 'Block Size', 'State', 'Health State',
                                 'Total Space', 'Used Space', 'Virtual IP'])
                cluster_name = json_response_dict.get('clusterName')
                cluster_type = json_response_dict.get('type')
                access_level = json_response_dict.get('clusterAccessLevel')
                created_time = utils.get_datetime_from_epoch(json_response_dict.get('clusterCreateTime'))
                updated_time = utils.get_datetime_from_epoch(json_response_dict.get('clusterUpdateTime'))
                min_cluster_size = json_response_dict.get('minClusterSize')
                replication_factor = json_response_dict.get('replicationFactor')
                block_size = json_response_dict.get('blockSize')
                total_space = utils.get_human_readable_size(json_response_dict.get('usableSpace'))
                used_space = utils.get_human_readable_size(json_response_dict.get('usedSpace'))
                virtual_ip = json_response_dict.get('virtualIp')
                cluster_state = json_response_dict.get('state')
                cluster_health_state = json_response_dict.get('healthState')

                t.add_row([cluster_name, cluster_type, access_level, created_time, updated_time,
                           min_cluster_size, replication_factor, block_size, cluster_state, cluster_health_state,
                           total_space, used_space, virtual_ip])
                print (t)
                return json_response_dict
            else:
                log.logger.exception(json_response_dict)
                raise Exception('Failed to get info for cluster {}'.format(cluster_id))
                

if  __name__ == "__main__":
    cluster_check = NJClusterTester()
    cluster_check.check_cluster_info()
                
                
            