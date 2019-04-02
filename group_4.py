from utils import DnaCenter
from utils import TestCase
import pprint
import responses
import requests

# define a pretty-printer for diagnostics
pp = pprint.PrettyPrinter(indent=4)

use_mock = False

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


@responses.activate
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
def tc_dna_intent_api_v1_network_device():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDevice',
                  yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/network-device')
    pp.pprint(response.json())

    # complete
    tc.okay('complete')


def run_all_tests():
    # run this test case first since it will do a basic 'ping'
    # tc_dna_intent_api_v1_network_device_count()

    # add new test cases to be run here
    #  tc_dna_intent_api_v1_interface()
    #  tc_dna_intent_api_v1_interface_network_device()
    tc_dna_intent_api_v1_interface_count()


#    tc_dna_intent_api_v1_network_device()


run_all_tests()
