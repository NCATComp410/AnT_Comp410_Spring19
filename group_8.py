from utils import DnaCenter
from utils import TestCase
import responses
import requests
import pprint

# define a pretty-printer for diagnostics
pp = pprint.PrettyPrinter(indent=4)

# This is a basic test case template included in each team's
# source code file.  Use this function as a template to build
# additional test cases
def tc_dna_intent_api_v1_network_device_count():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDeviceCount', yaml_file='params.yaml')

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


def get_unique_device_id(dnac):
    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/network-device')
    # pp.pprint(response.json())

    # get unique list of devices
    device_list = []
    for device in response.json()['response']:
        if device['id'] not in device_list:
            device_list.append(device['id'])
    return device_list

use_intent = True
if use_intent:
    intent_api = 'dna/intent/'
else:
    intent_api = ''

use_mock = True
@responses.activate

# dna/intent/api/v1/network-device/config
def tc_dna_intent_api_v1_network_device_config():
    # create this test case
 tc = TestCase(test_name='IntentApiV1NetworkDeviceConfig', yaml_file='params.yaml')
 response = None
 if not use_mock :
     # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    response = dnac.get('dna/intent/api/v1/network-device/config')
    print("dnac in use")
 else:
    print("dnac not in use")
    #json_mock ={'response': 4, 'version': '1.0'}
    json_mock = {'response': [
        {'type': 'Cisco ASR 1001-X Router', 'errorCode': None, 'family': 'Routers', 'location': None,
         'role': 'BORDER ROUTER', 'errorDescription': None, 'lastUpdateTime': 1548356572632,
         'lastUpdated': '2019-01-24 19:02:52', 'tagCount': '0',
         'inventoryStatusDetail': '<status><general code="SYNC"/></status>', 'macAddress': '00:c8:8b:80:bb:00',
         'hostname': 'asr1001-x', 'serialNumber': 'FXS1932Q1SE', 'softwareVersion': '16.3.2', 'locationName': None,
         'upTime': '69 days, 0:36:16.43', 'softwareType': 'IOS-XE', 'collectionInterval': 'Global Default',
         'roleSource': 'AUTO', 'apManagerInterfaceIp': '', 'associatedWlcIp': '',
         'bootDateTime': '2018-10-14 16:59:30', 'collectionStatus': 'In Progress', 'interfaceCount': '12',
         'lineCardCount': '9',
         'lineCardId': '19557762-4170-42c0-b4ae-c539ee996a05, 184ddd93-2fc2-4baa-aa66-67e4e2948399, c5987ca2-3f69-4341-8cf5-00431f3add0c, ab808a88-85a0-434f-895d-7b98cd0e25fb, 1e38a03d-c5dd-46dc-8038-74e83b3da5ca, ba411ee4-6e98-4bf4-afdd-1601fcc5b9e9, 454acd43-5b66-4912-a692-bb00a9725267, d5e53e21-6e3d-4e8f-881a-ea619b133511, f4fc3497-9624-44d1-b32e-4b074706727c',
         'managementIpAddress': '10.10.22.253', 'memorySize': '3819298032', 'platformId': 'ASR1001-X',
         'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable',
         'series': 'Cisco ASR 1000 Series Aggregation Services Routers', 'snmpContact': '', 'snmpLocation': '',
         'tunnelUdpPort': None, 'waasDeviceMode': None, 'instanceUuid': '1904ca0d-01be-4d13-88e5-4f4f9980b512',
         'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '1904ca0d-01be-4d13-88e5-4f4f9980b512'},
        {'type': 'Cisco Catalyst 9300 Switch', 'errorCode': None, 'family': 'Switches and Hubs', 'location': None,
         'role': 'ACCESS', 'errorDescription': None, 'lastUpdateTime': 1548357387166,
         'lastUpdated': '2019-01-24 19:16:27', 'tagCount': '0',
         'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>', 'macAddress': 'f8:7b:20:67:62:80',
         'hostname': 'cat_9k_1', 'serialNumber': 'FCW2136L0AK', 'softwareVersion': '16.6.1', 'locationName': None,
         'upTime': '69 days, 0:50:24.83', 'softwareType': 'IOS-XE', 'collectionInterval': 'Global Default',
         'roleSource': 'AUTO', 'apManagerInterfaceIp': '', 'associatedWlcIp': '',
         'bootDateTime': '2018-10-16 10:37:51', 'collectionStatus': 'Managed', 'interfaceCount': '41',
         'lineCardCount': '2',
         'lineCardId': 'df065d20-8d9b-4b66-a5ed-30aab545b85b, 766f14fe-8bb6-4ac7-a58c-f456f7e2ab34',
         'managementIpAddress': '10.10.22.66', 'memorySize': '889226872', 'platformId': 'C9300-24UX',
         'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable',
         'series': 'Cisco Catalyst 9300 Series Switches', 'snmpContact': '', 'snmpLocation': '',
         'tunnelUdpPort': None, 'waasDeviceMode': None, 'instanceUuid': '1a85db61-8bf2-4717-9060-9776f42e4581',
         'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '1a85db61-8bf2-4717-9060-9776f42e4581'},
        {'type': 'Cisco Catalyst 9300 Switch', 'errorCode': None, 'family': 'Switches and Hubs', 'location': None,
         'role': 'ACCESS', 'errorDescription': None, 'lastUpdateTime': 1548357386718,
         'lastUpdated': '2019-01-24 19:16:26', 'tagCount': '0',
         'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>', 'macAddress': 'f8:7b:20:71:4d:80',
         'hostname': 'cat_9k_2', 'serialNumber': 'FCW2140L039', 'softwareVersion': '16.6.1', 'locationName': None,
         'upTime': '100 days, 8:38:37.31', 'softwareType': 'IOS-XE', 'collectionInterval': 'Global Default',
         'roleSource': 'AUTO', 'apManagerInterfaceIp': '', 'associatedWlcIp': '',
         'bootDateTime': '2018-10-16 10:37:05', 'collectionStatus': 'Managed', 'interfaceCount': '41',
         'lineCardCount': '2',
         'lineCardId': 'fb1bc751-e9c3-4f76-8dd6-e1f8eb125f5d, 0c8e3427-8af1-4117-a1a1-d26f62fdba57',
         'managementIpAddress': '10.10.22.70', 'memorySize': '889226872', 'platformId': 'C9300-24UX',
         'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable',
         'series': 'Cisco Catalyst 9300 Series Switches', 'snmpContact': '', 'snmpLocation': '',
         'tunnelUdpPort': None, 'waasDeviceMode': None, 'instanceUuid': '2800864b-78ff-4bfd-9a60-83364d35c197',
         'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '2800864b-78ff-4bfd-9a60-83364d35c197'},
        {'type': 'Cisco Catalyst38xx stack-able ethernet switch', 'errorCode': None, 'family': 'Switches and Hubs',
         'location': None, 'role': 'DISTRIBUTION', 'errorDescription': None, 'lastUpdateTime': 1548357236629,
         'lastUpdated': '2019-01-24 19:13:56', 'tagCount': '0',
         'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>', 'macAddress': 'cc:d8:c1:15:d2:80',
         'hostname': 'cs3850', 'serialNumber': 'FOC1833X0AR', 'softwareVersion': '16.6.2s', 'locationName': None,
         'upTime': '100 days, 8:34:29.53', 'softwareType': 'IOS-XE', 'collectionInterval': 'Global Default',
         'roleSource': 'AUTO', 'apManagerInterfaceIp': '', 'associatedWlcIp': '',
         'bootDateTime': '2018-10-16 10:40:12', 'collectionStatus': 'Managed', 'interfaceCount': '59',
         'lineCardCount': '2',
         'lineCardId': '529ae584-3c97-492d-bad0-a79e25be334b, a7b77de2-a3dd-400d-a826-6c1ae387a555',
         'managementIpAddress': '10.10.22.73', 'memorySize': '873744896', 'platformId': 'WS-C3850-48U-E',
         'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable',
         'series': 'Cisco Catalyst 3850 Series Ethernet Stackable Switch', 'snmpContact': '', 'snmpLocation': '',
         'tunnelUdpPort': None, 'waasDeviceMode': None, 'instanceUuid': '79d3a90b-1b95-4cd8-a9bd-6d5952814432',
         'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '79d3a90b-1b95-4cd8-a9bd-6d5952814432'}],
        'version': '1.0'}

    rest_cmd = intent_api + 'api/v1/network-device'

    # execute the command and get response
    responses.add(responses.GET, 'http://' + rest_cmd,
                  json=json_mock,
                  status=200)
    response = requests.get('http://' + rest_cmd)


 if response.status_code == 200:
        print("Correct status code")
        print("Status code =",response.status_code)
    #pp.pprint(response.json())
 else:
        print("Incorrect status code")
        print("Status code =", response.status_code)
 # complete
 tc.okay('complete')

def tc_dna_intent_api_v1_network_device_config_count():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDeviceConfigCount', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/network-device/config/count')
    if response.status_code == 200:
        print("Correct status code")
        print("Status code =",response.status_code)
    # pp.pprint(response.json())
    else:
        print("Incorrect status code")
        print("Status code =", response.status_code)

    # complete
    tc.okay('complete')


def tc_dna_intent_api_v1_network_device_config_device():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDeviceConfigDevice', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    device_list = get_unique_device_id(dnac)

    for device_id in device_list:
        response = dnac.get('dna/intent/api/v1/network-device/' + device_id + '/config')
        if response.status_code == 200:
            print("Correct status code")
            print("Status code =", response.status_code)
        # pp.pprint(response.json())
        else:
            print("Incorrect status code")
            print("Status code =", response.status_code)

    # complete
    tc.okay('complete')


def run_all_tests():
    # run this test case first since it will do a basic 'ping'
    #tc_dna_intent_api_v1_network_device_count()



    # add test cases to these methods
    tc_dna_intent_api_v1_network_device_config()
    #tc_dna_intent_api_v1_network_device_config_count()
    #tc_dna_intent_api_v1_network_device_config_device()




run_all_tests()
