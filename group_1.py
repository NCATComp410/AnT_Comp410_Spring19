from utils import DnaCenter
from utils import TestCase
from utils import is_valid_ipv4_address
from utils import is_valid_32h_id
import pprint
import responses
import requests

# define a pretty-printer for diagnostics
pp = pprint.PrettyPrinter(indent=4)

# Add ability to fall-back to older API
use_intent = True

if use_intent:
    intent_api = 'dna/intent/'
else:
    intent_api = ''

# This is a basic test case template included in each team's
# source code file.  Use this function as a template to build
# additional test cases
def tc_dna_intent_api_v1_network_device_count():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDeviceCount', yaml_file='params.yaml')
    tc.okay('starting')

    rest_cmd = 'dna/intent/api/v1/network-device/count'

    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # execute the command and get response
        response = dnac.get(rest_cmd)
    else:
        json_mock = {'response': 4, 'version': '1.0'}
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)

    # Check to see if a response other than 200-OK was received
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
        # check to make sure there is at least 1 device present to work with
        device_count = response.json()['response']
        if device_count:
            tc.okay(f'found {device_count} total devices')
        else:
            # If no devices were found it's a pretty good bet that most/all remaining
            # tests will fail, so, consider this a critical failure and abort here by
            # setting abort=True
            tc.fail('no devices were found', abort=True)

        # check the version
        expected_version = tc.params['IntentApiV1NetworkDeviceCount']['Version']
        actual_version = response.json()['version']
        if expected_version == actual_version:
            tc.okay('correct version found')
        else:
            tc.fail(f'expected version {expected_version} instead found {actual_version}')


def tc_dna_intent_api_vi_topology_l2_vlan():
    # create this test case
    tc = TestCase(test_name='IntentApiV1TopologyL2Vlan', yaml_file='params.yaml')

    # REST API command to be executed
    rest_cmd = intent_api + 'api/v1/topology/vlan/vlan-names'

    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # find available vlan names
        response = dnac.get(rest_cmd)

    else:
        json_mock = {'response': ['Vlan1'], 'version': '1.0'}
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)

    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code), True)

    # get additional information about each vlan
    for vlan_name in response.json()['response']:
        rest_cmd = intent_api + 'api/v1/topology/l2/Vlan1'
        if not use_mock:
            response = dnac.get(rest_cmd)
        else:
            json_mock = {'response':
                             {'nodes':
                                  [{'deviceType': 'Cisco ASR 1001-X Router',
                                    'label': 'asr1001-x.abc.inc',
                                    'ip': '10.10.22.253',
                                    'softwareVersion': '16.3.2',
                                    'greyOut': True,
                                    'nodeType': 'device',
                                    'family': 'Routers',
                                    'platformId': 'ASR1001-X',
                                    'tags': [],
                                    'role': 'BORDER ROUTER',
                                    'roleSource': 'AUTO',
                                    'customParam': {},
                                    'additionalInfo': {'macAddress': '00:c8:8b:80:bb:00',
                                                       'latitude': '',
                                                       'siteid': '80023cfe-7ae1-4c71-9f41-7602fec88f9a',
                                                       'fabricRoles': ['BORDER', 'MAPSERVER', 'INTERMEDIATE'],
                                                       'longitude': ''},
                                    'id': '1904ca0d-01be-4d13-88e5-4f4f9980b512'},
                                   {'deviceType': 'Cisco Catalyst 9300 Switch',
                                    'label': 'cat_9k_1.marius.x-trem.ro',
                                    'ip': '10.10.22.66',
                                    'softwareVersion': '16.6.1',
                                    'nodeType': 'device',
                                    'family': 'Switches and Hubs',
                                    'platformId': 'C9300-24UX',
                                    'tags': [],
                                    'role': 'ACCESS',
                                    'roleSource': 'AUTO',
                                    'customParam': {},
                                    'additional.Info': {'macAddress': 'f8:7b:20:67:62:80',
                                                        'latitude': '',
                                                        'siteid': '80023cfe-7ae1-4c71-9f41-7602fec88f9a',
                                                        'longitude': ''},
                                    'id': '1a85db61-8bf2-4717-9060-9776f42e4581'},
                                   {'deviceType': 'Cisco Catalyst 9300 Switch',
                                    'label': 'cat_9k_2.marius.x-trem.ro',
                                    'ip': '10.10.22.70', 'softwareVersion':
                                        '16.6.4a',
                                    'nodeType': 'device',
                                    'family': 'Switches and Hubs',
                                    'platformId': 'C9300-24UX',
                                    'tags': [],
                                    'role': 'ACCESS',
                                    'roleSource': 'AUTO',
                                    'customParam': {},
                                    'additionalInfo': {'macAddress': 'f8:7b:20:71:4d:80',
                                                       'latitude': '',
                                                       'siteid': '80023cfe-7ae1-4c71-9f41-7602fec88f9a',
                                                       'longitude': ''},
                                    'id': '2800864b-78ff-4bfd-9a60-83364d35c197'},
                                   {'deviceType': 'Cisco Catalyst38xx stack-able ethernet switch',
                                    'label': 'cs3850.marius.x-trem.ro',
                                    'ip': '10.10.22.73', 'softwareVersion': '16.6.2s',
                                    'nodeType': 'device', 'family': 'Switches and Hubs',
                                    'platformId': 'WS-C3850-48U-E', 'tags': [],
                                    'role': 'DISTRIBUTION', 'roleSource': 'AUTO',
                                    'customParam': {},
                                    'additionalInfo': {'macAddress': 'cc:d8:c1:15:d2:80',
                                                       'latitude': '',
                                                       'siteid': '80023cfe-7ae1-4c71-9f41-7602fec88f9a',
                                                       'fabricRoles': ['EDGE', 'BORDER', 'MAPSERVER', 'INTERMEDIATE'],
                                                       'longitude': ''},
                                    'id': '79d3a90b-1b95-4cd8-a9bd-6d5952814432'},
                                   {'deviceType': 'wired', 'label': '10.10.22.98',
                                    'ip': '10.10.22.98',
                                    'greyOut': True,
                                    'nodeType': 'HOST',
                                    'family': 'WIRED',
                                    'role': 'HOST',
                                    'customParam': {},
                                    'additionalInfo': {'macAddress': 'c8:4c:75:68:b2:c0'},
                                    'id': 'a6fb899d-acd2-47ca-90e6-063e82086a05'},
                                   {'deviceType': 'wired',
                                    'label': '10.10.22.114',
                                    'ip': '10.10.22.114',
                                    'greyOut': True,
                                    'nodeType': 'HOST',
                                    'family': 'WIRED',
                                    'role': 'HOST',
                                    'customParam': {},
                                    'additionalInfo': {'macAddress': '00:1e:13:a5:b9:40'},
                                    'id': 'ff8a838d-fb47-40d7-8a57-7a5189ceb185'},
                                   {'deviceType': 'cloud node',
                                    'label': 'cloud node',
                                    'ip': 'UNKNOWN',
                                    'softwareVersion': 'UNKNOWN',
                                    'greyOut': True,
                                    'nodeType': 'cloud node',
                                    'family': 'cloud node',
                                    'platformId': 'UNKNOWN',
                                    'tags': ['cloud node'],
                                    'role': 'cloud node',
                                    'roleSource': 'AUTO',
                                    'customParam': {},
                                    'id': '0c8414c1-e2f5-4e72-97ec-3e99188eb47e'}],
                              'links': [{'source': '1a85db61-8bf2-4717-9060-9776f42e4581',
                                         'startPortID': '8352aa72-4851-4023-a765-d07004f6e524',
                                         'startPortName': 'TenGigabitEthernet1/1/1',
                                         'startPortIpv4Address': '10.10.22.66',
                                         'startPortIpv4Mask': '255.255.255.252',
                                         'startPortSpeed': '10000000',
                                         'target': '79d3a90b-1b95-4cd8-a9bd-6d5952814432',
                                         'endPortID': '36002b06-ae27-413c-9b36-ee1195e5af02',
                                         'endPortName': 'TenGigabitEthernet1/1/2',
                                         'endPortIpv4Address': '10.10.22.65',
                                         'endPortIpv4Mask': '255.255.255.252',
                                         'endPortSpeed': '10000000',
                                         'linkStatus': 'up',
                                         'greyOut': True,
                                         'additionalInfo': {},
                                         'id': '409414'},
                                        {'source': '2800864b-78ff-4bfd-9a60-83364d35c197',
                                         'startPortID': 'dc03baa0-8a80-406d-99ec-c94d6b33b35a',
                                         'startPortName': 'TenGigabitEthernet1/1/1',
                                         'startPortIpv4Address': '10.10.22.70',
                                         'startPortIpv4Mask': '255.255.255.252',
                                         'startPortSpeed': '10000000',
                                         'target': '79d3a90b-1b95-4cd8-a9bd-6d5952814432',
                                         'endPortID': 'd336120c-e616-462d-8053-210ff653da79',
                                         'endPortName': 'TenGigabitEthernet1/1/3',
                                         'endPortIpv4Address': '10.10.22.69',
                                         'endPortIpv4Mask': '255.255.255.252',
                                         'endPortSpeed': '10000000',
                                         'linkStatus': 'up',
                                         'greyOut': True,
                                         'additionalInfo': {},
                                         'id': '409413'},
                                        {'source': '1904ca0d-01be-4d13-88e5-4f4f9980b512',
                                         'startPortID': '5891c30f-af17-4c04-8101-8dbb76ad770e',
                                         'startPortName': 'TenGigabitEthernet0/0/1',
                                         'startPortIpv4Address': '10.10.22.74',
                                         'startPortIpv4Mask': '255.255.255.252',
                                         'startPortSpeed': '10000000',
                                         'target': '79d3a90b-1b95-4cd8-a9bd-6d5952814432',
                                         'endPortID': 'afea66a1-8d56-4897-b1a9-5349e513602c',
                                         'endPortName': 'TenGigabitEthernet1/1/1',
                                         'endPortIpv4Address': '10.10.22.73',
                                         'endPortIpv4Mask': '255.255.255.252',
                                         'endPortSpeed': '10000000',
                                         'linkStatus': 'up',
                                         'greyOut': True,
                                         'additionalInfo': {},
                                         'id': '409415'},
                                        {'source': '1a85db61-8bf2-4717-9060-9776f42e4581',
                                         'startPortID': '92b04d61-fb13-432b-aade-b760929b3ff3',
                                         'target': 'a6fb899d-acd2-47ca-90e6-063e82086a05',
                                         'linkStatus': 'UP',
                                         'greyOut': True,
                                         'additionalInfo': {}},
                                        {'source': '2800864b-78ff-4bfd-9a60-83364d35c197',
                                         'startPortID': '48a8c168-d850-4493-981b-feef4e471847',
                                         'target': 'ff8a838d-fb47-40d7-8a57-7a5189ceb185',
                                         'linkStatus': 'UP',
                                         'greyOut': True,
                                         'additionalInfo': {}},
                                        {'source': '0c8414c1-e2f5-4e72-97ec-3e99188eb47e',
                                         'target': '1904ca0d-01be-4d13-88e5-4f4f9980b512',
                                         'linkStatus': 'up',
                                         'greyOut': True}]},
                         'version': '1.0'}
            responses.add(responses.GET, 'http://' + rest_cmd,
                          json=json_mock,
                          status=200)
            response = requests.get('http://' + rest_cmd)
        if response.status_code != 200:
            # this test should fail if any other response code received
            tc.fail('expected 200-OK actual response was ' + str(response.status_code), True)
        else:
            pp.pprint(response.json())

        # Get a list of available fields from the response for each device
        check_fields = True
        expected_node_fields = ['deviceType', 'label', 'ip', 'greyOut','softwareVersion', 'nodeType', 'family', 'platformId',
                                'tags', 'role', 'roleSource', 'customParam', 'additionalInfo', 'id']
        data = response.json()['response']
        for node in data['nodes']:
            node_fields = node.keys()
            for field in expected_node_fields:
                if field not in node_fields:
                    tc.fail(node['label'] + ':' + field + ' was expected but not found in the DNA-C results')
                    check_fields = False
                else:
                    tc.okay(node['label'] + ':Found expected field:' + field)

        expected_link_fields = ['source', 'startPortID', 'startPortName', 'startPortIpv4Address', 'startPortIpv4Mask',
                                'startPortSpeed',
                                'target', 'endPortID', 'endPortName', 'endPortIpv4Address', 'endPortIpv4Mask',
                                'endPortSpeed', 'linkStatus', 'additionalInfo', 'id']

        # Check that all expected fields for a link are present
        for link in data['links']:
            link_fields = link.keys()
            for field in expected_link_fields:
                if field not in link_fields:
                    tc.fail(link['source'] + ':' + field + ' was expected but not found in the DNA-C results')
                    check_fields = False
                else:
                    tc.okay(link['source'] + ':Found expected field:' + field)

        # Check if the response has an API version field
        if 'version' in response.json():
            tc.okay('found expected field version')
        else:
            pp.pprint('version field was expected but not found in the DNA-C results')
            check_fields = False

        # If all fields checked out OK
        if check_fields:
            tc.okay('all expected device fields were found')
        else:
            tc.fail('all expected device fields not found')
    # test complete
    tc.okay('complete')


def tc_dna_intent_api_vi_topology_site_topology():
    # create this test case
    tc = TestCase(test_name='IntentApiV1SiteTopology', yaml_file='params.yaml')
    # REST API command to be executed
    rest_cmd = intent_api + 'api/v1/topology/site-topology'


    if not use_mock:
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
               port=tc.params['DnaCenter']['Port'],
               username=tc.params['DnaCenter']['Username'],
               password=tc.params['DnaCenter']['Password'])

    # get site topology
        response = dnac.get(rest_cmd)
    # The json_mock is something which was saved in responses.log during a successful session
    else:
        json_mock = {'response': {
            'sites': [{'id': '21b35880-e95b-4a4e-a9a0-d1944b9fd89f','name': 'Area01',
                       'parentId': '574acdc5-1cf8-41e9-9df4-eb91940e30a9',
                       'latitude': '', 'longitude': '',
                       'locationType':'area',
                       'locationAddress': '',
                       'locationCountry': '',
                       'displayName': '437439',
                       'groupNameHierarchy': 'Global/Area01'},
            {'id': '91e8c93e-c332-4195-9a7d-96d4eaa7fbc1',
                   'name': 'Building01',
                   'parentId': '21b35880-e95b-4a4e-a9a0-d1944b9fd89f',
                   'latitude': '45.158349', 'longitude': '1.538086',
                   'locationType': 'building',
                   'locationAddress': 'Address Unknown',
                   'locationCountry': 'France',
                   'displayName': '437440',
                   'groupNameHierarchy': 'Global/Area01/Building01'},
                  {'id': '234b4aee-7469-4dc1-a841-fa03cf23c336',
                   'name': 'Melbourne',
                   'parentId': '574acdc5-1cf8-41e9-9df4-eb91940e30a9',
                   'latitude': '', 'longitude': '',
                   'locationType': 'area',
                   'locationAddress': '',
                   'locationCountry': '',
                   'displayName': '349349',
                   'groupNameHierarchy': 'Global/Melbourne'},
                  {'id': '4a0a3d40-1dc4-4dc7-b077-9bb067c6f0e9',
                   'name': 'MEL1',
                   'parentId': '234b4aee-7469-4dc1-a841-fa03cf23c336',
                   'latitude': '-37.815090',
                   'longitude': '144.970439',
                   'locationType': 'building',
                   'locationAddress': '101 Collins Street, Melbourne Victoria 3000, Australia',
                   'locationCountry': 'Australia',
                   'displayName': '349351',
                   'groupNameHierarchy': 'Global/Melbourne/MEL1'},
                  {'id': '99d3cf59-ce3f-4d39-a140-85755e154a51',
                   'name': 'Zurich',
                   'parentId': '574acdc5-1cf8-41e9-9df4-eb91940e30a9',
                   'latitude': '', 'longitude': '',
                   'locationType': 'area',
                   'locationAddress': '',
                   'locationCountry': '',
                   'displayName': '437441',
                   'groupNameHierarchy': 'Global/Zurich'},
                  {'id': 'f90f9069-443c-40c5-9c91-33537424be07',
                   'name': 'Sydney',
                   'parentId': '574acdc5-1cf8-41e9-9df4-eb91940e30a9',
                   'latitude': '',
                   'longitude': '',
                   'locationType': 'area',
                   'locationAddress': '',
                   'locationCountry': '',
                   'displayName': '349350',
                   'groupNameHierarchy': 'Global/Sydney'},
                  {'id': '85e138ea-da55-4608-87db-76c11e316493',
                   'name': 'SYD1',
                   'parentId': 'f90f9069-443c-40c5-9c91-33537424be07',
                   'latitude': '-33.837053', 'longitude': '151.206266',
                   'locationType': 'building',
                   'locationAddress': '177 Pacific Highway, North Sydney New South Wales 2060, Australia',
                   'locationCountry': 'Australia',
                   'displayName': '349352',
                   'groupNameHierarchy': 'Global/Sydney/SYD1'},
                  {'id': '55194d84-2634-4286-ace0-46a98d9016dd',
                   'name': 'WLSN',
                   'parentId': '99d3cf59-ce3f-4d39-a140-85755e154a51',
                   'latitude': '47.410171', 'longitude': '8.591671',
                   'locationType': 'building',
                   'locationAddress': 'Richtistrasse, 8304 Wallisellen, Switzerland',
                   'locationCountry': 'Switzerland',
                   'displayName': '437442',
                   'groupNameHierarchy': 'Global/Zurich/WLSN'},
                  {'id': '0a08655d-4c36-4cf8-a70c-916f8c054040',
                   'name': 'Brisbane',
                   'parentId': '574acdc5-1cf8-41e9-9df4-eb91940e30a9',
                   'latitude': '', 'longitude': '',
                   'locationType': 'area',
                   'locationAddress': '',
                   'locationCountry': '',
                   'displayName': '437449',
                   'groupNameHierarchy': 'Global/Brisbane'},
                  {'id': '404de111-ac74-4d14-8b3f-3dbae63e4e59',
                   'name': 'PAR1',
                   'parentId': '5f5a4971-a022-4166-bca4-27c860080675',
                   'latitude': '', 'longitude': '',
                   'locationType': 'area',
                   'locationAddress': '',
                   'locationCountry': '',
                   'displayName': '437451',
                   'groupNameHierarchy': 'Global/France/PAR1'},
                  {'id': '60334acd-a445-42b2-852c-f3e9700ee463',
                   'name': 'Honolulu, HI',
                   'parentId': '574acdc5-1cf8-41e9-9df4-eb91940e30a9',
                   'latitude': '', 'longitude': '',
                   'locationType': 'area',
                   'locationAddress': '',
                   'locationCountry': '',
                   'displayName': '437457',
                   'groupNameHierarchy': 'Global/Honolulu, HI'},
                  {'id': 'c331e545-ff1d-41ae-a7e4-2c2cfdaffefc',
                   'name': 'PARB1',
                   'parentId': '404de111-ac74-4d14-8b3f-3dbae63e4e59',
                   'latitude': '48.877361', 'longitude': '2.348328',
                   'locationType': 'building',
                   'locationAddress': 'Address Unknown',
                   'locationCountry': 'France',
                   'displayName': '437452',
                   'groupNameHierarchy': 'Global/France/PAR1/PARB1'},
                  {'id': '80023cfe-7ae1-4c71-9f41-7602fec88f9a',
                   'name': 'floor3',
                   'parentId': '55194d84-2634-4286-ace0-46a98d9016dd',
                   'latitude': '', 'longitude': '',
                   'locationType': 'floor',
                   'locationAddress': 'Richtistrasse, 8304 Wallisellen, Switzerland',
                   'locationCountry': '',
                   'displayName': '437443',
                   'groupNameHierarchy': 'Global/Zurich/WLSN/floor3'},
                  {'id': '9c3b1446-50c4-4f77-84df-c23ce3356224',
                   'name': 'Budapest',
                   'parentId': '574acdc5-1cf8-41e9-9df4-eb91940e30a9',
                   'latitude': '', 'longitude': '',
                   'locationType': 'area',
                   'locationAddress': '',
                   'locationCountry': '',
                   'displayName': '437444',
                   'groupNameHierarchy': 'Global/Budapest'},
                  {'id': 'ab19b31f-f98b-463e-91e1-238dabf17d0c',
                   'name': 'HillSide',
                   'parentId': '9c3b1446-50c4-4f77-84df-c23ce3356224',
                   'latitude': '47.489630', 'longitude': '19.023943',
                   'locationType': 'building',
                   'locationAddress': 'Address Unknown',
                   'locationCountry': 'Hungary',
                   'displayName': '437445',
                   'groupNameHierarchy': 'Global/Budapest/HillSide'},
                  {'id': 'b251f7f2-ce0a-45fc-93ed-81b9655d4d69',
                   'name': 'Floor 6.',
                   'parentId': 'ab19b31f-f98b-463e-91e1-238dabf17d0c',
                   'latitude': '', 'longitude': '',
                   'locationType': 'floor',
                   'locationAddress': 'Address Unknown',
                   'locationCountry': '',
                   'displayName': '437446',
                   'groupNameHierarchy': 'Global/Budapest/HillSide/Floor 6.'},
                  {'id': 'cc2c0027-8d63-4deb-b99d-d62bb711081b',
                   'name': 'Test Lux',
                   'parentId': '574acdc5-1cf8-41e9-9df4-eb91940e30a9',
                   'latitude': '', 'longitude': '',
                   'locationType': 'area',
                   'locationAddress': '',
                   'locationCountry': '',
                   'displayName': '437448',
                   'groupNameHierarchy': 'Global/Test Lux'},
                  {'id': '5f5a4971-a022-4166-bca4-27c860080675',
                   'name': 'France',
                   'parentId': '574acdc5-1cf8-41e9-9df4-eb91940e30a9',
                   'latitude': '', 'longitude': '',
                   'locationType': 'area',
                   'locationAddress': '',
                   'locationCountry': '',
                   'displayName': '437450',
                   'groupNameHierarchy': 'Global/France'},
                  {'id': '6c891f8f-66ec-42b4-999c-1c95ddcafcb8',
                   'name': 'Corporate',
                   'parentId': 'cdf3573c-08d4-4630-b0db-4f35a8c7585f',
                   'latitude': '33.914457', 'longitude': '-84.337573',
                   'locationType': 'building',
                   'locationAddress': '4170 Ashford Dunwoody Road Northeast, Atlanta, Georgia 30319, United States',
                   'locationCountry': 'United States',
                   'displayName': '437454',
                   'groupNameHierarchy': 'Global/Atlanta/Corporate'},
                  {'id': 'cdf3573c-08d4-4630-b0db-4f35a8c7585f',
                   'name': 'Atlanta',
                   'parentId': '574acdc5-1cf8-41e9-9df4-eb91940e30a9',
                   'latitude': '', 'longitude': '',
                   'locationType': 'area',
                   'locationAddress': '',
                   'locationCountry': '',
                   'displayName': '437453',
                   'groupNameHierarchy': 'Global/Atlanta'},
                  {'id': '59a46e0b-fa50-46d0-9b40-3a01b630aca4',
                   'name': 'Floor 2',
                   'parentId': '6c891f8f-66ec-42b4-999c-1c95ddcafcb8',
                   'latitude': '', 'longitude': '',
                   'locationType': 'floor',
                   'locationAddress': '4170 Ashford Dunwoody Road Northeast, Atlanta, Georgia 30319, United States',
                   'locationCountry': '',
                   'displayName': '437455',
                   'groupNameHierarchy': 'Global/Atlanta/Corporate/Floor 2'}]},
        'version': '1.0'}
        responses.add(responses.GET, 'http://' + rest_cmd,
                  json=json_mock,
                  status=200)
        response = requests.get('http://' + rest_cmd)

    # Check to see if a response other than 200-OK was received
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code), True)
    else:
        pp.pprint(response.json())

    # find unique countries
    country_list = []
    for site in response.json()['response']['sites']:
        if site['locationCountry']:
            if not site['locationCountry'] in country_list:
                country_list.append(site['locationCountry'])
    tc.okay('countries found:' + ','.join(country_list))

    # Get a list of available fields from the response for each device
    check_fields = True
    expected_site_fields =['id', 'name', 'parentId', 'latitude','longitude', 'locationType',
                   'locationAddress','locationCountry', 'displayName', 'groupNameHierarchy' ]

    # Check that all expected fields for a node are present
    data = response.json()['response']
    for site in data['sites']:
        site_fields = site.keys()
        for field in expected_site_fields:
            if field not in site_fields:
                tc.fail(site['locationCountry'] + ':' + field + ' was expected but not found in the DNA-C results')
                check_fields = False
            else:
                tc.okay(site['locationCountry'] + ':Found expected field:' + field)

                if field == 'id':
                    if is_valid_32h_id(site['id']):
                        tc.okay(site['id'] + ' is a valid id')
                    else:
                        tc.fail(site['id'] + " INVALID id")

                # Check if the response has an API version field
                if 'version' in response.json():
                    tc.okay('found expected field version')
                else:
                    pp.pprint('version field was expected but not found in the DNA-C results')
                    check_fields = False

                # If all fields checked out OK
                if check_fields:
                    tc.okay('all expected device fields were found')
                else:
                    tc.fail('all expected device fields not found')

    # test complete
    tc.okay('complete')


def tc_dna_intent_api_vi_topology_physical_topology():
    # create this test case
    tc = TestCase(test_name='IntentApiV1PhysicalTopology', yaml_file='params.yaml')

    # REST API comment to be executed
    rest_cmd = intent_api + 'api/v1/topology/physical-topology'

    tc.okay('starting')

    # If not using mock, create a DNA-C session and make request
    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # get physical topology
        response = dnac.get(rest_cmd)
    # If using mock, create JSON response and create response
    else:
        json_mock = {'response':
                         {'nodes':
                              [{'deviceType': 'Cisco Catalyst 9300 Switch',
                                'label': 'cat_9k_1.abc.inc',
                                'ip': '10.10.22.66',
                                'softwareVersion': '16.6.1',
                                'nodeType': 'device',
                                'family': 'Switches and Hubs',
                                'platformId': 'C9300-24UX',
                                'tags': [],
                                'role': 'ACCESS',
                                'roleSource': 'AUTO',
                                'customParam': {},
                                'additionalInfo': {'macAddress': 'f8:7b:20:67:62:80',
                                                   'latitude': '',
                                                   'siteid': 'ee07dfe5-d673-40a8-9c00-75e6c5ebd3e1',
                                                   'longitude': ''},
                                'id': '3360f852-63af-4e08-b3f8-0d98ca7d416d'},
                               {'deviceType': 'Cisco ASR 1001-X Router',
                                'label': 'asr1001-x.contoso.net',
                                'ip': '10.10.22.253',
                                'softwareVersion': '16.3.2',
                                'nodeType': 'device',
                                'family': 'Routers',
                                'platformId': 'ASR1001-X',
                                'tags': [],
                                'role': 'CORE',
                                'roleSource': 'MANUAL',
                                'customParam': {},
                                'additionalInfo': {'macAddress': '00:c8:8b:80:bb:00',
                                                   'latitude': '43.613283',
                                                   'siteid': '5d307104-4381-4d4f-b626-9aac981ee973',
                                                   'fabricRoles': ['BORDER', 'MAPSERVER', 'INTERMEDIATE'],
                                                   'longitude': '-79.740686'},
                                'id': '55f2d416-255f-45ac-91cc-72be6e6aeb97'},
                               {'deviceType': 'Cisco Catalyst38xx stack-able ethernet switch',
                                'label': 'cs3850.contoso.net',
                                'ip': '10.10.22.73',
                                'softwareVersion': '16.6.2s',
                                'nodeType': 'device',
                                'family': 'Switches and Hubs',
                                'platformId': 'WS-C3850-48U-E',
                                'tags': [],
                                'role': 'CORE',
                                'roleSource': 'MANUAL',
                                'customParam': {},
                                'additionalInfo': {'macAddress': 'cc:d8:c1:15:d2:80',
                                                   'latitude': '46.048246',
                                                   'siteid': '3b1cb361-80f9-45e3-9899-31956cb890b2',
                                                   'fabricRoles': ['EDGE', 'BORDER', 'MAPSERVER', 'INTERMEDIATE'],
                                                   'longitude': '14.456806'},
                                'id': '7b101af0-1bcf-4158-9639-cf09b3e8bea9'},
                               {'deviceType': 'wired',
                                'label': '10.10.22.98',
                                'ip': '10.10.22.98',
                                'nodeType': 'HOST',
                                'family': 'WIRED',
                                'role': 'HOST',
                                'customParam': {},
                                'additionalInfo': {'macAddress': 'c8:4c:75:68:b2:c0'},
                                'id': '566aa099-2717-4197-b53e-653b19d09ff1'},
                               {'deviceType': 'Cisco Catalyst 9300 Switch',
                                'label': 'cat_9k_2',
                                'ip': '10.10.22.70',
                                'softwareVersion': '16.6.4a',
                                'nodeType': 'device',
                                'family': 'Switches and Hubs',
                                'platformId': 'C9300-24UX',
                                'tags': [],
                                'role': 'ACCESS',
                                'roleSource': 'AUTO',
                                'customParam': {},
                                'additionalInfo': {'macAddress': 'f8:7b:20:71:4d:80'},
                                'id': '805cb36a-cab1-48b9-a304-85b47854b49d'},
                               {'deviceType': 'wired',
                                'label': '10.10.22.114',
                                'ip': '10.10.22.114',
                                'nodeType': 'HOST',
                                'family': 'WIRED',
                                'role': 'HOST',
                                'customParam': {},
                                'additionalInfo': {'macAddress': '00:1e:13:a5:b9:40'},
                                'id': '6e1ebf28-7f6b-46b5-b305-320342243af7'}],
                          'links': [{'source': '3360f852-63af-4e08-b3f8-0d98ca7d416d',
                                     'startPortID': '1e1609d6-cdb2-4327-a801-0d5a042f1f65',
                                     'startPortName': 'TenGigabitEthernet1/1/1',
                                     'startPortIpv4Address': '10.10.22.66',
                                     'startPortIpv4Mask': '255.255.255.252',
                                     'startPortSpeed': '10000000',
                                     'target': '7b101af0-1bcf-4158-9639-cf09b3e8bea9',
                                     'endPortID': '35c35993-3b88-4af5-a152-af384737e096',
                                     'endPortName': 'TenGigabitEthernet1/1/2',
                                     'endPortIpv4Address': '10.10.22.65',
                                     'endPortIpv4Mask': '255.255.255.252',
                                     'endPortSpeed': '10000000',
                                     'linkStatus': 'up',
                                     'additionalInfo': {},
                                     'id': '426467'},
                                    {'source': '55f2d416-255f-45ac-91cc-72be6e6aeb97',
                                     'startPortID': 'a86fff62-ed69-40da-967b-6e99f1a004a9',
                                     'startPortName': 'TenGigabitEthernet0/0/1',
                                     'startPortIpv4Address': '10.10.22.74',
                                     'startPortIpv4Mask': '255.255.255.252',
                                     'startPortSpeed': '10000000',
                                     'target': '7b101af0-1bcf-4158-9639-cf09b3e8bea9',
                                     'endPortID': '71646f86-8a8b-4337-9c0e-d8642a5236af',
                                     'endPortName': 'TenGigabitEthernet1/1/1',
                                     'endPortIpv4Address': '10.10.22.73',
                                     'endPortIpv4Mask': '255.255.255.252',
                                     'endPortSpeed': '10000000',
                                     'linkStatus': 'up',
                                     'additionalInfo': {},
                                     'id': '426464'},
                                    {'source': '3360f852-63af-4e08-b3f8-0d98ca7d416d',
                                     'startPortID': '8f9085c7-33c7-4732-8fb7-ead0329abe13',
                                     'target': '566aa099-2717-4197-b53e-653b19d09ff1',
                                     'linkStatus': 'UP',
                                     'additionalInfo': {}},
                                    {'source': '805cb36a-cab1-48b9-a304-85b47854b49d',
                                     'startPortID': '8b87970a-a591-43e0-935e-76f5c36c4738',
                                     'startPortName': 'TenGigabitEthernet1/1/1',
                                     'startPortIpv4Address': '10.10.22.70',
                                     'startPortIpv4Mask': '255.255.255.252',
                                     'startPortSpeed': '10000000',
                                     'target': '7b101af0-1bcf-4158-9639-cf09b3e8bea9',
                                     'endPortID': '2a6e1fee-5ec0-4826-ad98-27a2ad37ea28',
                                     'endPortName': 'TenGigabitEthernet1/1/3',
                                     'endPortIpv4Address': '10.10.22.69',
                                     'endPortIpv4Mask': '255.255.255.252',
                                     'endPortSpeed': '10000000',
                                     'linkStatus': 'up',
                                     'additionalInfo': {},
                                     'id': '426466'},
                                    {'source': '805cb36a-cab1-48b9-a304-85b47854b49d',
                                     'startPortID': '12a91929-3ce5-4528-91ec-4b4d1dce3943',
                                     'target': '6e1ebf28-7f6b-46b5-b305-320342243af7',
                                     'linkStatus': 'UP',
                                     'additionalInfo': {}}]},
                     'version': '1.0'}
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json = json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)

    # Check to see if a response other than 200-OK was received
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code), True)
    else:
        pp.pprint(response.json())

    # Get a list of available fields from the response for each device
    check_fields = True
    expected_node_fields = ['deviceType', 'label', 'ip', 'softwareVersion', 'nodeType', 'family', 'platformId',
                                'tags', 'role', 'roleSource', 'customParam', 'additionalInfo', 'id']
    # Check that all expected fields for a node are present
    data = response.json()['response']
    for node in data['nodes']:
        node_fields = node.keys()
        for field in expected_node_fields:
            if field not in node_fields:
                tc.fail(node['label'] + ':' + field + ' was expected but not found in the DNA-C results')
                check_fields = False
            else:
                tc.okay(node['label'] + ':Found expected field:' + field)
                if field == 'ip':
                    if is_valid_ipv4_address(node['ip']):
                        tc.okay(node['ip'] + ' is a valid address')
                    else:
                        tc.fail(node['ip'] + " INVALID address")


    expected_link_fields = ['source', 'startPortID', 'startPortName', 'startPortIpv4Address', 'startPortIpv4Mask', 'startPortSpeed',
            'target', 'endPortID', 'endPortName', 'endPortIpv4Address', 'endPortIpv4Mask', 'endPortSpeed', 'linkStatus', 'additionalInfo', 'id']

    # If all node fields checked out OK
    if check_fields:
        tc.okay('all expected node fields were found')
    else:
        tc.fail('all expected node fields not found')

    # Set check fields back to true for checking link
    check_fields = True;
        
    # Check that all expected fields for a link are present
    for link in data['links']:
        link_fields = link.keys()
        for field in expected_link_fields:
            if field not in link_fields:
                tc.fail(link['source'] + ':' + field + ' was expected but not found in the DNA-C results')
                check_fields = False
            else:
                tc.okay(link['source'] + ':Found expected field:' + field)
                if field == 'startPortIpv4Address':
                    if is_valid_ipv4_address(link['startPortIpv4Address']):
                        tc.okay(link['startPortIpv4Address'] + ' is a valid address')
                    else:
                        tc.fail(link['startPortIpv4Address'] + ' INVALID address')
                if field == 'endPortIpv4Address':
                    if is_valid_ipv4_address(link['endPortIpv4Address']):
                        tc.okay(link['endPortIpv4Address'] + ' is a valid address')
                    else:
                        tc.fail(link['endPortIpv4Address'] + ' INVALID address')

    # If all link fields checked out OK
    if check_fields:
        tc.okay('all expected link fields were found')
    else:
        tc.fail('all expected link fields not found')

    # Check if the response has an API version field
    if 'version' in response.json():
        tc.okay('found expected field version')
    else:
        tc.fail('version field was expected but not found in the DNA-C results')

    # test complete
    tc.okay('complete')


# To use the mock you need to do two things
#
# (1) Be sure to set use_mock = True
#     For normal operation use_mock = False
#     Don't check-in the code with use_mock = True!
use_mock = False
#
# (2) Uncomment the following line to activate the responses module:
#@responses.activate
#
# Once these two things have been done you will use the mock instead
# of the real DNA-C.  It's important to know how do this since the
# real DNA-C could become unavailable and you'll need to use the mock
# to make progress on your assignments.
#
# *** Normally you should not check-in the code with the mock enabled! ***
#
def run_all_tests():
    # print a warning whenever using the mock
    if use_mock:
        print('use_mock is set to True - WARNING - Using the MOCK!')
    else:
        print('use_mock is set to False - Using DNA-C')

    # run this test case first since it will do a basic 'ping'
    tc_dna_intent_api_v1_network_device_count()

    # add new test cases to be run here
    tc_dna_intent_api_vi_topology_l2_vlan()
    tc_dna_intent_api_vi_topology_site_topology()
    tc_dna_intent_api_vi_topology_physical_topology()


run_all_tests()

