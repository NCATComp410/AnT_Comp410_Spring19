from utils import DnaCenter, is_valid_macAddress
from utils import TestCase
import pprint
import responses
import requests

# define a pretty-printer for diagnostics
pp = pprint.PrettyPrinter(indent=4)

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

# dna/intent/api/v1/interface
def tc_dna_intent_api_v1_interface():
    # create this test case
    tc = TestCase(test_name='IntentApiV1Interface', yaml_file='params.yaml')
    rest_cmd = intent_api + 'api/v1/interface'

    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])
        # get site interface
        # execute the command and get response
        # response = dnac.get('dna/intent/api/v1/interface')
        response = dnac.get(rest_cmd)
        pp.pprint(response.json())
    else:
        json_mock = {'response': [{
            "adminStatus": "string",
            "className": "string",
            "description": "string",
            "deviceId": "string",
            "duplex": "string",
            "id": "string",
            "ifIndex": "string",
            "instanceTenantId": "string",
            "instanceUuid": "string",
            "interfaceType": "string",
            "ipv4Address": "string",
            "ipv4Mask": "string",
            "isisSupport": "string",
            "lastUpdated": "string",
            "macAddress": "string",
            "mappedPhysicalInterfaceId": "string",
            "mappedPhysicalInterfaceName": "string",
            "mediaType": "string",
            "nativeVlanId": "string",
            "ospfSupport": "string",
            "pid": "string",
            "portMode": "string",
            "portName": "string",
            "portType": "string",
            "serialNo": "string",
            "series": "string",
            "speed": "string",
            "status": "string",
            "vlanId": "string",
            "voiceVlan": "string"
          }
        ],
            "version": "string"
     }

        responses.add(responses.GET, 'http://' + rest_cmd, json=json_mock, status=200)
        response = requests.get('http://' + rest_cmd)

    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
        pp.pprint(response.json())

        check_fields = True
        expected_fields = ['adminStatus', 'className', 'description', 'deviceId', 'duplex', 'id', 'ifIndex', 'instanceTenantId', 'instanceUuid', 'interfaceType', 'ipv4Address', 'ipv4Mask', 'isisSupport', 'lastUpdated', 'macAddress', 'mappedPhysicalInterfaceId', 'mappedPhysicalInterfaceName', 'mediaType', 'nativeVlanId', 'ospfSupport', 'pid', 'portMode', 'portName', 'portType', 'serialNo', 'series', 'speed', 'status', 'vlanId', 'voiceVlan']
        for device in response.json()['response']:
            device_fields = device.keys()
            for field in expected_fields:
                if field not in device_fields:
                    tc.fail(field + ' was expected but not found in the DNA-C results')
                    check_fields = False
                else:
                    tc.okay(':Found expected field:' + field)

            # If all fields checked out OK
        if check_fields:
            tc.okay('all expected device fields were found')

        for device in response.json()['response']:
            pp.pprint(device.keys);
        # complete
        #Sprint 4 - check the format content of macAddress

        if is_valid_macAddress(device['macAddress']):
            tc.okay(device['macAddress'] + ' is a valid macAddress')

        else:
            tc.fail(device['macAddress'] + ' is NOT a valid macAddress')
        tc.okay('complete')


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
    tc = TestCase(test_name='IntentApiV1InterfaceCount',
                  yaml_file='params.yaml')
    rest_cmd = intent_api + 'api/v1/interface/count'

    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])
        # get site interface count
        response = dnac.get(rest_cmd)
    else:
        json_mock = {'response': 112, 'version': '1.0'}

        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)

        response = requests.get('http://' + rest_cmd)

    pp.pprint(response.json())
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' +
                str(response.status_code))
    else:
        # check to make sure there is at least 1 device present to work with
        interface_count = response.json()['response']
        if interface_count:
            tc.okay('found {} total interfaces'.format(interface_count))
        else:
            # If no devices were found it's a pretty good bet that most/all remaining
            # tests will fail, so, consider this a critical failure and abort here by
            # setting abort=True
            tc.fail('no devices were found', abort=True)

    check_fields = True
    check_values = True
    expected_keys = ['response', 'version']

    for key in expected_keys:
        if key not in response.json():
            tc.fail(key + ':' + 'was expected but not found in the DNA=C results')
            check_fields = False

    if check_fields:
        tc.okay('all expected device fields were found')
    else:
        tc.fail('all expected device fields not found')

    if not str(response.json()['response']).isdigit():
        tc.fail("numeric value was expected to be a number but instead got: " + response.json()['response'])
        check_values = False

    if not str(response.json()['version']) == '1.0':
        tc.fail("1.0 was expected to be the value of Version but instead got: " + response.json()['response'])
        check_values = False

    if check_values:
        tc.okay('all fields had their expected values')
    else:
        tc.fail('all or some fields had unexpected values')

    # test complete
    tc.okay('complete')


# dna/intent/api/v1/network-device
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
        json_mock = {'response': [{'roleSource': 'AUTO', 'associatedWlcIp': '', 'bootDateTime': '2019-02-19 19:40:52',
                                   'collectionStatus': 'Managed', 'family': 'Switches and Hubs', 'interfaceCount': '59',
                                   'lineCardCount': '2',
                                   'lineCardId': 'f0665a2b-82f5-470d-b8ce-f684e19f87d3, '
                                                 '31db9454-d1c5-45a1-bcba-5b4742c0682d',
                                   'managementIpAddress': '10.10.22.73', 'memorySize': '873744896',
                                   'platformId': 'WS-C3850-48U-E', 'reachabilityFailureReason': '',
                                   'reachabilityStatus': 'Reachable',
                                   'series': 'Cisco Catalyst 3850 Series Ethernet Stackable Switch', 'snmpContact': '',
                                   'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None,
                                   'apManagerInterfaceIp': '', 'errorCode': None,
                                   'type': 'Cisco Catalyst38xx stack-able ethernet switch', 'location': None,
                                   'role': 'DISTRIBUTION', 'upTime': '6 days, 1:38:42.81', 'errorDescription': None,
                                   'lastUpdateTime': 1554130060502, 'softwareType': 'IOS-XE',
                                   'serialNumber': 'FOC1833X0AR', 'softwareVersion': '16.6.2s',
                                   'lastUpdated': '2019-04-01 14:47:40', 'hostname': 'Adam_TEST.corpaa.aa.com',
                                   'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>',
                                   'tagCount': '0', 'macAddress': 'cc:d8:c1:15:d2:80', 'locationName': None,
                                   'collectionInterval': 'Global Default',
                                   'instanceUuid': '7bce6b93-2c1f-4bfc-9383-bfdeb4d819dd',
                                   'instanceTenantId': '5bd3634ab2bea0004c3ebb58',
                                   'id': '7bce6b93-2c1f-4bfc-9383-bfdeb4d819dd'},
                                  {'roleSource': 'AUTO', 'associatedWlcIp': '', 'bootDateTime': '2019-02-20 15:15:25',
                                   'collectionStatus': 'In Progress', 'family': 'Switches and Hubs',
                                   'interfaceCount': '41', 'lineCardCount': '2',
                                   'lineCardId': '98d722c0-9b3f-4d34-817b-71e0601ffc5e, '
                                                 '090f9ad3-2c08-4de6-8bb0-721795597392',
                                   'managementIpAddress': '10.10.22.66', 'memorySize': '889226872',
                                   'platformId': 'C9300-24UX', 'reachabilityFailureReason': '',
                                   'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 9300 Series Switches',
                                   'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None,
                                   'apManagerInterfaceIp': '', 'errorCode': None, 'type': 'Cisco Catalyst 9300 Switch',
                                   'location': None, 'role': 'ACCESS', 'upTime': '39 days, 23:12:08.95',
                                   'errorDescription': None, 'lastUpdateTime': 1554128820850, 'softwareType': 'IOS-XE',
                                   'serialNumber': 'FCW2136L0AK', 'softwareVersion': '16.6.1',
                                   'lastUpdated': '2019-04-01 14:27:00', 'hostname': 'Adam_TEST.corpaa.aa.com',
                                   'inventoryStatusDetail': '<status><general code="SYNC"/></status>', 'tagCount': '0',
                                   'macAddress': 'f8:7b:20:67:62:80', 'locationName': None,
                                   'collectionInterval': 'Global Default',
                                   'instanceUuid': '21107199-8940-4a8a-99f2-6067ab925f6d',
                                   'instanceTenantId': '5bd3634ab2bea0004c3ebb58',
                                   'id': '21107199-8940-4a8a-99f2-6067ab925f6d'},
                                  {'roleSource': 'AUTO', 'associatedWlcIp': '', 'bootDateTime': '2019-02-19 19:44:10',
                                   'collectionStatus': 'Managed', 'family': 'Switches and Hubs', 'interfaceCount': '41',
                                   'lineCardCount': '2',
                                   'lineCardId': 'facf605f-696d-4905-88ea-2d5a4af0344e, '
                                                 '240100d8-7e15-43f9-94a4-797f530ab0a3',
                                   'managementIpAddress': '10.10.22.70', 'memorySize': '1425966824',
                                   'platformId': 'C9300-24UX', 'reachabilityFailureReason': '',
                                   'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 9300 Series Switches',
                                   'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None,
                                   'apManagerInterfaceIp': '', 'errorCode': None, 'type': 'Cisco Catalyst 9300 Switch',
                                   'location': None, 'role': 'ACCESS', 'upTime': '40 days, 18:57:21.50',
                                   'errorDescription': None, 'lastUpdateTime': 1554129817999, 'softwareType': 'IOS-XE',
                                   'serialNumber': 'FCW2140L039', 'softwareVersion': '16.6.4a',
                                   'lastUpdated': '2019-04-01 14:43:37', 'hostname': 'Adam_TEST.corpaa.aa.com',
                                   'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>',
                                   'tagCount': '0', 'macAddress': 'f8:7b:20:71:4d:80', 'locationName': None,
                                   'collectionInterval': 'Global Default',
                                   'instanceUuid': '026bc0a3-4e2f-4deb-8f11-6bd005ca3c7b',
                                   'instanceTenantId': '5bd3634ab2bea0004c3ebb58',
                                   'id': '026bc0a3-4e2f-4deb-8f11-6bd005ca3c7b'}], 'version': '1.0'}

        responses.add(responses.GET, 'http://' + rest_cmd, json=json_mock, status=200)
        response = requests.get('http://' + rest_cmd)

    pp.pprint(response.json())

    for device in response.json()['response']:
        pp.pprint(device.keys())
    # complete
    tc.okay('complete')


# To use the mock you need to do two things
#
# (1) Be sure to set use_mock = True
#     For normal operation use_mock = False
#     Don't check-in the code with use_mock = True!
use_mock = False


#
# (2) Uncomment the following line to activate the responses module:
# @responses.activate
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
    #tc_dna_intent_api_v1_network_device_count()

    # add new test cases to be run here
    tc_dna_intent_api_v1_interface()
    #tc_dna_intent_api_v1_interface_network_device()
    #tc_dna_intent_api_v1_interface_count()
    #tc_dna_intent_api_v1_network_device()


run_all_tests()





