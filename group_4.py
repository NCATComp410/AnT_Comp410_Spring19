from utils import DnaCenter
from utils import TestCase
import pprint
import responses
import requests

# define a pretty-printer for diagnostics
pp = pprint.PrettyPrinter(indent=4)

# In order to use a mock two things must be done:
# (1) Set use_mock = True
# When use_mock = False you will use the real DNA-C
use_mock = True

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
    tc = TestCase(test_name='IntentApiV1NetworkDeviceCount',
                  yaml_file='params.yaml')

    rest_cmd = tc_dna_intent_api_v1_interface_count

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])
    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/network-device/count')

    # Check to see if a response other than 200-OK was received
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' +
                str(response.status_code))

    else:
        # check to make sure there is at least 1 device present to work with
        device_count = response.json()['response']

        if device_count:
            tc.okay('found {}  total devices'.format(device_count))
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
            tc.fail(
                'expected version {} instead found {} '.format(expected_version, actual_version))


# dna/intent/api/v1/interface
def tc_dna_intent_api_v1_interface():
    # create this test case
    tc = TestCase(test_name='IntentApiV1Interface', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/interface')
    pp.pprint(response.json())

    # complete
    tc.okay('complete')


# @responses.activate
def tc_dna_intent_api_v1_interface_network_device():
    # create this test case
    tc = TestCase(test_name='IntentApiV1InterfaceNetworkDevice',
                  yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/interface')

    # get unique list of deviceId
    device_list = []
    device_count = 0
    for device in response.json()['response']:
        if device['deviceId'] not in device_list:
            device_count += 1
            device_list.append(device['deviceId'])
    tc.okay('found {} devices:' + ','.join(device_list).format(device_count))

    for device_id in device_list:
        response = dnac.get(
            'dna/intent/api/v1/interface/network-device/' + device_id)
        pp.pprint(response.json())

    # complete
    tc.okay('complete')


# /dna/intent/api/v1/interface/count
def tc_dna_intent_api_v1_interface_count():
    # create this test case
    tc = TestCase(test_name='IntentApiV1InterfaceNetworkDeviceCount',
                  yaml_file='params.yaml')
    rest_cmd = intent_api + 'api/v1/interface/count'

    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])
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
                      json=json_mock,
                      status=200)

    # response = requests.get('http://' + rest_cmd)

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])
    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/interface/count')
    pp.pprint(response.json())

    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' +
                str(response.status_code))
    else:
        # check to make sure there is at least 1 device present to work with
        device_count = response.json()['response']
        if device_count:
            tc.okay('found {} total devices'.format(device_count))
        else:
            # If no devices were found it's a pretty good bet that most/all remaining
            # tests will fail, so, consider this a critical failure and abort here by
            # setting abort=True
            tc.fail('no devices were found', abort=True)

    # list all interfaces and count them
    response = dnac.get('dna/intent/api/v1/interface')
    print(len(response.json()['response']))

    tc.okay('complete')


# dna/intent/api/v1/network-device
# To use the mock you need to do two things
# (1) scroll up to the top of the file and make sure use_mock = True
# (2) Uncomment the following line to activate the responses module:
# @responses.activate
def tc_dna_intent_api_v1_network_device():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDevice',
                  yaml_file='params.yaml')

    rest_cmd = 'dna/intent/api/v1/network-device'

    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # execute the command and get response
        response = dnac.get(rest_cmd)
    else:
        json_mock = {'response': [{'roleSource': 'AUTO', 'associatedWlcIp': '', 'bootDateTime': '2019-02-19 19:40:52', 'collectionStatus': 'Managed', 'family': 'Switches and Hubs', 'interfaceCount': '59', 'lineCardCount': '2', 'lineCardId': 'f0665a2b-82f5-470d-b8ce-f684e19f87d3, 31db9454-d1c5-45a1-bcba-5b4742c0682d', 'managementIpAddress': '10.10.22.73', 'memorySize': '873744896', 'platformId': 'WS-C3850-48U-E', 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 3850 Series Ethernet Stackable Switch', 'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'apManagerInterfaceIp': '', 'errorCode': None, 'type': 'Cisco Catalyst38xx stack-able ethernet switch', 'location': None, 'role': 'DISTRIBUTION', 'upTime': '6 days, 1:38:42.81', 'errorDescription': None, 'lastUpdateTime': 1554130060502, 'softwareType': 'IOS-XE', 'serialNumber': 'FOC1833X0AR', 'softwareVersion': '16.6.2s', 'lastUpdated': '2019-04-01 14:47:40', 'hostname': 'Adam_TEST.corpaa.aa.com', 'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>', 'tagCount': '0', 'macAddress': 'cc:d8:c1:15:d2:80', 'locationName': None, 'collectionInterval': 'Global Default', 'instanceUuid': '7bce6b93-2c1f-4bfc-9383-bfdeb4d819dd', 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '7bce6b93-2c1f-4bfc-9383-bfdeb4d819dd'}, {'roleSource': 'AUTO', 'associatedWlcIp': '', 'bootDateTime': '2019-02-20 15:15:25', 'collectionStatus': 'In Progress', 'family': 'Switches and Hubs', 'interfaceCount': '41', 'lineCardCount': '2', 'lineCardId': '98d722c0-9b3f-4d34-817b-71e0601ffc5e, 090f9ad3-2c08-4de6-8bb0-721795597392', 'managementIpAddress': '10.10.22.66', 'memorySize': '889226872', 'platformId': 'C9300-24UX', 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 9300 Series Switches', 'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'apManagerInterfaceIp': '', 'errorCode': None, 'type': 'Cisco Catalyst 9300 Switch', 'location': None, 'role': 'ACCESS', 'upTime': '39 days, 23:12:08.95', 'errorDescription': None, 'lastUpdateTime': 1554128820850, 'softwareType': 'IOS-XE', 'serialNumber': 'FCW2136L0AK', 'softwareVersion': '16.6.1', 'lastUpdated': '2019-04-01 14:27:00', 'hostname': 'Adam_TEST.corpaa.aa.com', 'inventoryStatusDetail': '<status><general code="SYNC"/></status>', 'tagCount': '0', 'macAddress': 'f8:7b:20:67:62:80', 'locationName': None, 'collectionInterval': 'Global Default', 'instanceUuid': '21107199-8940-4a8a-99f2-6067ab925f6d', 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '21107199-8940-4a8a-99f2-6067ab925f6d'}, {'roleSource': 'AUTO', 'associatedWlcIp': '', 'bootDateTime': '2019-02-19 19:44:10', 'collectionStatus': 'Managed', 'family': 'Switches and Hubs', 'interfaceCount': '41', 'lineCardCount': '2', 'lineCardId': 'facf605f-696d-4905-88ea-2d5a4af0344e, 240100d8-7e15-43f9-94a4-797f530ab0a3', 'managementIpAddress': '10.10.22.70', 'memorySize': '1425966824', 'platformId': 'C9300-24UX', 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 9300 Series Switches', 'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'apManagerInterfaceIp': '', 'errorCode': None, 'type': 'Cisco Catalyst 9300 Switch', 'location': None, 'role': 'ACCESS', 'upTime': '40 days, 18:57:21.50', 'errorDescription': None, 'lastUpdateTime': 1554129817999, 'softwareType': 'IOS-XE', 'serialNumber': 'FCW2140L039', 'softwareVersion': '16.6.4a', 'lastUpdated': '2019-04-01 14:43:37', 'hostname': 'Adam_TEST.corpaa.aa.com', 'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>', 'tagCount': '0', 'macAddress': 'f8:7b:20:71:4d:80', 'locationName': None, 'collectionInterval': 'Global Default', 'instanceUuid': '026bc0a3-4e2f-4deb-8f11-6bd005ca3c7b', 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '026bc0a3-4e2f-4deb-8f11-6bd005ca3c7b'}], 'version': '1.0'}

        responses.add(responses.GET, 'http://' + rest_cmd, json=json_mock, status=200)
        response = requests.get('http://' + rest_cmd)

    pp.pprint(response.json())

    for device in response.json()['response']:
        print(device.keys())

    # complete
    tc.okay('complete')


def run_all_tests():
    # run this test case first since it will do a basic 'ping'
    # tc_dna_intent_api_v1_network_device_count()

    # add new test cases to be run here
    #  tc_dna_intent_api_v1_interface()
    #  tc_dna_intent_api_v1_interface_network_device()
    # tc_dna_intent_api_v1_interface_count()

    tc_dna_intent_api_v1_network_device()


run_all_tests()
