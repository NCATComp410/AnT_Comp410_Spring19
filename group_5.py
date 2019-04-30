from utils import DnaCenter
from utils import TestCase
import pprint
import responses
import requests
from utils import is_valid_ipv4_address


# define a pretty-printer for diagnostics
pp = pprint.PrettyPrinter(indent=4)


use_intent = True

if use_intent:
    intent_api = 'dna/intent/'
else:
    intent_api = ''


def tc_dna_intent_api_v1_network_device():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDevice', yaml_file='params.yaml')

    # REST API command to be executed
    rest_cmd = intent_api + 'api/v1/network-device'

    if not use_mock:
        # In this case we don't want to use a mock and will create a normal session to the dnac
        # create a session to the DNA-C and get a response back
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # get list of all network devices
        response = dnac.get(rest_cmd)
    else:
        # In this case we're going to use a mock and not actually communicate with the DNA-C
        # The json_mock is something which was saved in responses.log during a successful session
        # It is much easier to build this way than to build it from scratch!
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

        # instead of actually talking to the DNA-C we're going to mock-up the response
        # this command inserts our mock-up which will be retrieved by response as though it was real
        # try changing the response code to something other than 200 to test out that part of the code
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)

    # Following code gets processed normally with or without the mock in place
    # Check to see if a response other than 200-OK was received
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
        # there is no point in continuing this test case so return here
        return

    # get list of all host names and serial numbers
    # that are present in the response
    host_list = []
    serialNumber_list = []
    for device in response.json()['response']:
        if device['hostname']:
            host_list.append(device['hostname'])
            serialNumber_list.append(device['serialNumber'])

    # list of hosts and serial numbers found
    print('Hosts Found:')
    pp.pprint(host_list)
    print(','.join(host_list))
    print('Serial Numbers:')
    pp.pprint(serialNumber_list)
    
    # Get a list of available fields from the response for each device
    check_fields = True
    expected_fields = ['type', 'errorCode', 'family', 'location', 'role', 'errorDescription', 'lastUpdateTime', 'lastUpdated', 'tagCount', 'inventoryStatusDetail', 'macAddress', 'hostname', 'serialNumber', 'softwareVersion', 'locationName', 'upTime', 'softwareType', 'collectionInterval', 'roleSource', 'apManagerInterfaceIp', 'associatedWlcIp', 'bootDateTime', 'collectionStatus', 'interfaceCount', 'lineCardCount', 'lineCardId', 'managementIpAddress', 'memorySize', 'platformId', 'reachabilityFailureReason', 'reachabilityStatus', 'series', 'snmpContact', 'snmpLocation', 'tunnelUdpPort', 'waasDeviceMode', 'instanceUuid', 'instanceTenantId', 'id']
    for device in response.json()['response']:
        device_fields = device.keys()
        for field in expected_fields:
            if field not in device_fields:
                tc.fail(device['hostname'] + ':' + field + ' was expected but not found in the DNA-C results')
                check_fields = False
            else:
                tc.okay(device['hostname'] + ':Found expected field:' + field)

    # If all fields checked out OK
    if check_fields:
        tc.okay('all expected device fields were found')

    # The host list has changed frequently in the sandbox which makes maintaining
    # this test step unrealistic, so, commenting it out for now
    #
    # get list of expected host names from the parameters files
    # expected_hosts = tc.params['IntentApiV1NetworkDevice']['Hosts'].split(',')
    # hosts_ok = True
    # for h in expected_hosts:
        # if we find an expected host that is not in the actual hosts from the response
        # this is a failure
    #    if h not in host_list:
    #        tc.fail(h + ' not in host_list')
    #        hosts_ok = False
    # if hosts_ok:
    #    tc.okay('found all expected hosts:' + ' '.join(host_list))

    # make sure serialNumber parameter works
    sn_ok = True
    for sn in serialNumber_list:
        rest_cmd = intent_api + 'api/v1/network-device'

        if not use_mock:
            response = dnac.get(rest_cmd, params={'serialNumber': sn})
        else:
            # create a separate mock for each serial number we've learned
            json_mock['FXS1932Q1SE'] = {'response': [
                {'type': 'Cisco ASR 1001-X Router', 'errorCode': None, 'family': 'Routers', 'location': None,
                 'role': 'BORDER ROUTER', 'errorDescription': None, 'lastUpdateTime': 1548356572632,
                 'lastUpdated': '2019-01-24 19:02:52', 'tagCount': '0',
                 'inventoryStatusDetail': '<status><general code="SYNC"/></status>', 'macAddress': '00:c8:8b:80:bb:00',
                 'hostname': 'asr1001-x', 'serialNumber': 'FXS1932Q1SE', 'softwareVersion': '16.3.2',
                 'locationName': None, 'upTime': '69 days, 0:36:16.43', 'softwareType': 'IOS-XE',
                 'collectionInterval': 'Global Default', 'roleSource': 'AUTO', 'apManagerInterfaceIp': '',
                 'associatedWlcIp': '', 'bootDateTime': '2018-10-14 16:59:30', 'collectionStatus': 'In Progress',
                 'interfaceCount': '12', 'lineCardCount': '9',
                 'lineCardId': '19557762-4170-42c0-b4ae-c539ee996a05, 184ddd93-2fc2-4baa-aa66-67e4e2948399, c5987ca2-3f69-4341-8cf5-00431f3add0c, ab808a88-85a0-434f-895d-7b98cd0e25fb, 1e38a03d-c5dd-46dc-8038-74e83b3da5ca, ba411ee4-6e98-4bf4-afdd-1601fcc5b9e9, 454acd43-5b66-4912-a692-bb00a9725267, d5e53e21-6e3d-4e8f-881a-ea619b133511, f4fc3497-9624-44d1-b32e-4b074706727c',
                 'managementIpAddress': '10.10.22.253', 'memorySize': '3819298032', 'platformId': 'ASR1001-X',
                 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable',
                 'series': 'Cisco ASR 1000 Series Aggregation Services Routers', 'snmpContact': '', 'snmpLocation': '',
                 'tunnelUdpPort': None, 'waasDeviceMode': None, 'instanceUuid': '1904ca0d-01be-4d13-88e5-4f4f9980b512',
                 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '1904ca0d-01be-4d13-88e5-4f4f9980b512'}],
                                        'version': '1.0'}
            json_mock['FCW2136L0AK'] = {'response': [
                {'type': 'Cisco Catalyst 9300 Switch', 'errorCode': None, 'family': 'Switches and Hubs',
                 'location': None, 'role': 'ACCESS', 'errorDescription': None, 'lastUpdateTime': 1548357387166,
                 'lastUpdated': '2019-01-24 19:16:27', 'tagCount': '0',
                 'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>',
                 'macAddress': 'f8:7b:20:67:62:80', 'hostname': 'cat_9k_1', 'serialNumber': 'FCW2136L0AK',
                 'softwareVersion': '16.6.1', 'locationName': None, 'upTime': '69 days, 0:50:24.83',
                 'softwareType': 'IOS-XE', 'collectionInterval': 'Global Default', 'roleSource': 'AUTO',
                 'apManagerInterfaceIp': '', 'associatedWlcIp': '', 'bootDateTime': '2018-10-16 10:37:51',
                 'collectionStatus': 'Managed', 'interfaceCount': '41', 'lineCardCount': '2',
                 'lineCardId': 'df065d20-8d9b-4b66-a5ed-30aab545b85b, 766f14fe-8bb6-4ac7-a58c-f456f7e2ab34',
                 'managementIpAddress': '10.10.22.66', 'memorySize': '889226872', 'platformId': 'C9300-24UX',
                 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable',
                 'series': 'Cisco Catalyst 9300 Series Switches', 'snmpContact': '', 'snmpLocation': '',
                 'tunnelUdpPort': None, 'waasDeviceMode': None, 'instanceUuid': '1a85db61-8bf2-4717-9060-9776f42e4581',
                 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '1a85db61-8bf2-4717-9060-9776f42e4581'}],
                                        'version': '1.0'}
            json_mock['FCW2140L039'] = {'response': [
                {'type': 'Cisco Catalyst 9300 Switch', 'errorCode': None, 'family': 'Switches and Hubs',
                 'location': None, 'role': 'ACCESS', 'errorDescription': None, 'lastUpdateTime': 1548357386718,
                 'lastUpdated': '2019-01-24 19:16:26', 'tagCount': '0',
                 'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>',
                 'macAddress': 'f8:7b:20:71:4d:80', 'hostname': 'cat_9k_2', 'serialNumber': 'FCW2140L039',
                 'softwareVersion': '16.6.1', 'locationName': None, 'upTime': '100 days, 8:38:37.31',
                 'softwareType': 'IOS-XE', 'collectionInterval': 'Global Default', 'roleSource': 'AUTO',
                 'apManagerInterfaceIp': '', 'associatedWlcIp': '', 'bootDateTime': '2018-10-16 10:37:05',
                 'collectionStatus': 'Managed', 'interfaceCount': '41', 'lineCardCount': '2',
                 'lineCardId': 'fb1bc751-e9c3-4f76-8dd6-e1f8eb125f5d, 0c8e3427-8af1-4117-a1a1-d26f62fdba57',
                 'managementIpAddress': '10.10.22.70', 'memorySize': '889226872', 'platformId': 'C9300-24UX',
                 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable',
                 'series': 'Cisco Catalyst 9300 Series Switches', 'snmpContact': '', 'snmpLocation': '',
                 'tunnelUdpPort': None, 'waasDeviceMode': None, 'instanceUuid': '2800864b-78ff-4bfd-9a60-83364d35c197',
                 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '2800864b-78ff-4bfd-9a60-83364d35c197'}],
                                        'version': '1.0'}
            json_mock['FOC1833X0AR'] = {'response': [
                {'type': 'Cisco Catalyst38xx stack-able ethernet switch', 'errorCode': None,
                 'family': 'Switches and Hubs', 'location': None, 'role': 'DISTRIBUTION', 'errorDescription': None,
                 'lastUpdateTime': 1548357236629, 'lastUpdated': '2019-01-24 19:13:56', 'tagCount': '0',
                 'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>',
                 'macAddress': 'cc:d8:c1:15:d2:80', 'hostname': 'cs3850', 'serialNumber': 'FOC1833X0AR',
                 'softwareVersion': '16.6.2s', 'locationName': None, 'upTime': '100 days, 8:34:29.53',
                 'softwareType': 'IOS-XE', 'collectionInterval': 'Global Default', 'roleSource': 'AUTO',
                 'apManagerInterfaceIp': '', 'associatedWlcIp': '', 'bootDateTime': '2018-10-16 10:40:12',
                 'collectionStatus': 'Managed', 'interfaceCount': '59', 'lineCardCount': '2',
                 'lineCardId': '529ae584-3c97-492d-bad0-a79e25be334b, a7b77de2-a3dd-400d-a826-6c1ae387a555',
                 'managementIpAddress': '10.10.22.73', 'memorySize': '873744896', 'platformId': 'WS-C3850-48U-E',
                 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable',
                 'series': 'Cisco Catalyst 3850 Series Ethernet Stackable Switch', 'snmpContact': '',
                 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None,
                 'instanceUuid': '79d3a90b-1b95-4cd8-a9bd-6d5952814432', 'instanceTenantId': '5bd3634ab2bea0004c3ebb58',
                 'id': '79d3a90b-1b95-4cd8-a9bd-6d5952814432'}], 'version': '1.0'}

            # create the mock url.  Note that responses does not seem to handle parameters - ie ?param=value
            # well so just use another / as a separator.  This work OK for the mock.
            rest_cmd_mock = 'http://' + rest_cmd + '/serialNumber=' + sn
            responses.add(responses.GET, rest_cmd_mock,
                          json=json_mock[sn],
                          status=200)
            response = requests.get(rest_cmd_mock)

        # expect a 200-OK
        if response.status_code != 200:
            tc.fail('serialNumber ' + sn + ' expected 200-OK actual response was ' + str(response.status_code))
            # don't return here like we did above - let's see if other serialNumbers are OK
        else:
            for device in response.json()['response']:
                # expect response to be restricted to only the serialNumber we requested
                # if it is not, this is a failure
                if sn != device['serialNumber']:
                    tc.fail('found unexpected serial number ' + sn)
                    pp.pprint(response.json())
                    sn_ok = False
                    
                    
                    # sprint #4 - check the format content of at least one field
                # In this example each device has a managementIpAddress
                # We'll check to make sure the format on this is correct
                # 'managementIpAddress': '10.10.22.70'
                # This is an example of an ipv4 ip address
                if is_valid_ipv4_address(device['managementIpAddress']):
                    tc.okay(device['managementIpAddress'] + ' is a valid address')
                else:
                    tc.fail(device['managementIpAddress'] + ' INVALID address')
                    
    if sn_ok:
        tc.okay('serial numbers correct')

    # try an invalid serial number
    rest_cmd = intent_api + 'api/v1/network-device'

    if not use_mock:
        response = dnac.get(rest_cmd, params={'serialNumber': 'invalid'})
    else:
        json_mock = {'response': [], 'version': '1.0'}
        rest_cmd_mock = 'http://' + rest_cmd + '/serialNumber=' + 'invalid'
        responses.add(responses.GET, rest_cmd_mock,
                      json=json_mock,
                      status=200)
        response = requests.get(rest_cmd_mock)

    # in this case we expect the response to be a 200-OK
    if response.status_code != 200:
        tc.fail('invalid serial number expected 200-OK actual response was ' + str(response.status_code))
    else:
        # expect an empty list in the response - if there is something else there need to fail
        if response.json()['response']:
            tc.fail('invalid serial number expected empty response')
            pp.pprint(response.json())
        else:
            tc.okay('invalid serial number check passed')
###############################


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


def tc_dna_intent_api_v1_network_device_collection_schedule_global():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDeviceCollectionScheduleGlobal', yaml_file='params.yaml')
    tc.okay('starting')

    rest_cmd = 'dna/intent/api/v1/network-device/collection-schedule/global'

    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # execute the command and get response
        response = dnac.get(rest_cmd)
    else:
        json_mock = {'response': 1500, 'version': '1.0'}
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)
        
    if response.status_code != 200:
        # this test should fail if any other response code received
       tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
        pp.pprint(response.json())
         # complete
        tc.okay('complete')
        # check to make sure there is at least 1 device present to work with
        device_count = response.json()['response']
        if device_count:
            tc.okay(f'found {device_count} total devices')
        else:
            # If no devices were found it's a pretty good bet that most/all remaining
            # tests will fail, so, consider this a critical failure and abort here by
            # setting abort=True
            tc.fail('no devices were found', abort=True)
    
   


def get_unique_device_id(dnac):
    
    tc = TestCase(test_name='IntentApiV1NetworkDeviceCount', yaml_file='params.yaml')
    rest_cmd = 'dna/intent/api/v1/network-device'
    if not use_mock:
        # execute the command and get response
        response = dnac.get(rest_cmd)
        # pp.pprint(response.json())
    else:
        json_mock = {'response': [{'roleSource': 'AUTO', 'associatedWlcIp': '', 'bootDateTime': '2019-02-19 19:40:52', 'collectionStatus': 'Managed', 'family': 'Switches and Hubs', 'interfaceCount': '59', 'lineCardCount': '2', 'lineCardId': 'f0665a2b-82f5-470d-b8ce-f684e19f87d3, 31db9454-d1c5-45a1-bcba-5b4742c0682d', 'managementIpAddress': '10.10.22.73', 'memorySize': '873744896', 'platformId': 'WS-C3850-48U-E', 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 3850 Series Ethernet Stackable Switch', 'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'apManagerInterfaceIp': '', 'errorCode': None, 'type': 'Cisco Catalyst38xx stack-able ethernet switch', 'location': None, 'role': 'DISTRIBUTION', 'upTime': '6 days, 1:38:42.81', 'errorDescription': None, 'lastUpdateTime': 1554130060502, 'softwareType': 'IOS-XE', 'serialNumber': 'FOC1833X0AR', 'softwareVersion': '16.6.2s', 'lastUpdated': '2019-04-01 14:47:40', 'hostname': 'Adam_TEST.corpaa.aa.com', 'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>', 'tagCount': '0', 'macAddress': 'cc:d8:c1:15:d2:80', 'locationName': None, 'collectionInterval': 'Global Default', 'instanceUuid': '7bce6b93-2c1f-4bfc-9383-bfdeb4d819dd', 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '7bce6b93-2c1f-4bfc-9383-bfdeb4d819dd'}, {'roleSource': 'AUTO', 'associatedWlcIp': '', 'bootDateTime': '2019-02-20 15:15:25', 'collectionStatus': 'Managed', 'family': 'Switches and Hubs', 'interfaceCount': '41', 'lineCardCount': '2', 'lineCardId': '98d722c0-9b3f-4d34-817b-71e0601ffc5e, 090f9ad3-2c08-4de6-8bb0-721795597392', 'managementIpAddress': '10.10.22.66', 'memorySize': '889226872', 'platformId': 'C9300-24UX', 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 9300 Series Switches', 'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'apManagerInterfaceIp': '', 'errorCode': None, 'type': 'Cisco Catalyst 9300 Switch', 'location': None, 'role': 'ACCESS', 'upTime': '39 days, 23:12:08.95', 'errorDescription': None, 'lastUpdateTime': 1554128820850, 'softwareType': 'IOS-XE', 'serialNumber': 'FCW2136L0AK', 'softwareVersion': '16.6.1', 'lastUpdated': '2019-04-01 14:27:00', 'hostname': 'Adam_TEST.corpaa.aa.com', 'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>', 'tagCount': '0', 'macAddress': 'f8:7b:20:67:62:80', 'locationName': None, 'collectionInterval': 'Global Default', 'instanceUuid': '21107199-8940-4a8a-99f2-6067ab925f6d', 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '21107199-8940-4a8a-99f2-6067ab925f6d'}, {'roleSource': 'AUTO', 'associatedWlcIp': '', 'bootDateTime': '2019-02-19 19:44:10', 'collectionStatus': 'Managed', 'family': 'Switches and Hubs', 'interfaceCount': '41', 'lineCardCount': '2', 'lineCardId': 'facf605f-696d-4905-88ea-2d5a4af0344e, 240100d8-7e15-43f9-94a4-797f530ab0a3', 'managementIpAddress': '10.10.22.70', 'memorySize': '1425966824', 'platformId': 'C9300-24UX', 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 9300 Series Switches', 'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'apManagerInterfaceIp': '', 'errorCode': None, 'type': 'Cisco Catalyst 9300 Switch', 'location': None, 'role': 'ACCESS', 'upTime': '40 days, 18:57:21.50', 'errorDescription': None, 'lastUpdateTime': 1554129817999, 'softwareType': 'IOS-XE', 'serialNumber': 'FCW2140L039', 'softwareVersion': '16.6.4a', 'lastUpdated': '2019-04-01 14:43:37', 'hostname': 'Adam_TEST.corpaa.aa.com', 'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>', 'tagCount': '0', 'macAddress': 'f8:7b:20:71:4d:80', 'locationName': None, 'collectionInterval': 'Global Default', 'instanceUuid': '026bc0a3-4e2f-4deb-8f11-6bd005ca3c7b', 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'id': '026bc0a3-4e2f-4deb-8f11-6bd005ca3c7b'}], 'version': '1.0'}
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

    # get unique list of devices
    device_list = []
    for device in response.json()['response']:
        if device['id'] not in device_list:
            device_list.append(device['id'])
    return device_list


# dna/intent/api/v1/network-device/${id}/vlan
def tc_dna_intent_api_v1_network_device_id_vlan():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDeviceIdVlan', yaml_file='params.yaml')
    tc.okay('starting')

    # This command must be executed in two steps
    # the first step is to get a list of the available network-devices
    rest_cmd = 'dna/intent/api/v1/network-device'
    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        device_list = get_unique_device_id(dnac)
    else:
        # When using the mock, pass a null value in place of the dnac
        device_list = get_unique_device_id(None)

    tc.okay('found ' + str(len(device_list)) + ' devices:' + ','.join(device_list))

    for device_id in device_list:
        rest_cmd = 'dna/intent/api/v1/network-device/' + device_id + '/vlan'
        if not use_mock:
            response = dnac.get(rest_cmd)
        else:
            # creating a mock here is more difficult.  For now will use a single response over and over
            json_mock = {'response': [{'vlanNumber': 1, 'numberOfIPs': 16, 'ipAddress': '10.10.22.97', 'prefix': '28', 'interfaceName': 'Vlan1', 'networkAddress': '10.10.22.96'}], 'version': '1.0'}
            responses.add(responses.GET, 'http://' + rest_cmd,
                          json=json_mock,
                          status=200)
            response = requests.get('http://' + rest_cmd)
           
            
            
        if response.status_code != 200:
            # this test should fail if any other response code received
            tc.fail('expected 200-OK actual response was ' + str(response.status_code))
        else:
           
            for field in response.json()['response']:
                # print list of fields found in this response
                print(field.keys())
            
    if sn_ok:
        tc.okay('serial numbers correct')
    # complete
    tc.okay('complete')


# dna/intent/api/v1/interface/network-device/${deviceId}/${startIndex}/${recordsToReturn}
def tc_dna_intent_api_v1_interface_network_device_range():
    # create this test case
    tc = TestCase(test_name='IntentApiV1InterfaceNetworkDeviceRange', yaml_file='params.yaml')
    tc.okay('starting')

    if not use_mock:
    # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        device_list = get_unique_device_id(dnac)
    else:
        device_list = get_unique_device_id(None)

    tc.okay('found ' + str(len(device_list)) + ' devices:' + ','.join(device_list))

    # startIndex and number of records to return will need to be tested
    start_index = 1
    records_to_return = 5
    for device_id in device_list:
        rest_cmd = f'dna/intent/api/v1/interface/network-device/{device_id}/{start_index}/{records_to_return}'
        if not use_mock:
            response = dnac.get(rest_cmd)
        else:
            # this will only mock a single device
            json_mock = {'response': [{'description': '', 'status': 'up', 'interfaceType': 'Virtual', 'className': 'IntrfcPrtclEndpnt', 'ifIndex': '9', 'macAddress': None, 'speed': '8000000', 'adminStatus': 'UP', 'vlanId': '0', 'deviceId': '1904ca0d-01be-4d13-88e5-4f4f9980b512', 'portName': 'Crypto-Engine0/0/8', 'duplex': None, 'lastUpdated': '2019-03-16 01:50:02.821', 'portMode': 'routed', 'portType': 'OTHER', 'mediaType': None, 'series': 'Cisco ASR 1000 Series Aggregation Services Routers', 'ipv4Address': None, 'ipv4Mask': None, 'isisSupport': 'false', 'mappedPhysicalInterfaceId': None, 'mappedPhysicalInterfaceName': None, 'nativeVlanId': None, 'ospfSupport': 'false', 'pid': 'ASR1001-X', 'serialNo': 'FXS1932Q1SE', 'voiceVlan': None, 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'instanceUuid': 'd79bd401-ea12-4902-9229-842b7bb70364', 'id': 'd79bd401-ea12-4902-9229-842b7bb70364'}, {'description': '', 'status': 'down', 'interfaceType': 'Physical', 'className': 'EthrntPrtclEndpntExtndd', 'ifIndex': '10', 'macAddress': '00:c8:8b:80:bb:40', 'speed': '1000000', 'adminStatus': 'DOWN', 'vlanId': '0', 'deviceId': '1904ca0d-01be-4d13-88e5-4f4f9980b512', 'portName': 'GigabitEthernet0', 'duplex': 'AutoNegotiate', 'lastUpdated': '2019-03-16 01:50:02.821', 'portMode': 'routed', 'portType': 'Ethernet Port', 'mediaType': 'RJ45', 'series': 'Cisco ASR 1000 Series Aggregation Services Routers', 'ipv4Address': None, 'ipv4Mask': None, 'isisSupport': 'false', 'mappedPhysicalInterfaceId': None, 'mappedPhysicalInterfaceName': None, 'nativeVlanId': None, 'ospfSupport': 'false', 'pid': 'ASR1001-X', 'serialNo': 'FXS1932Q1SE', 'voiceVlan': None, 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'instanceUuid': 'fb348b85-6515-4254-8531-33ff92a0b5a7', 'id': 'fb348b85-6515-4254-8531-33ff92a0b5a7'}, {'description': '', 'status': 'down', 'interfaceType': 'Physical', 'className': 'EthrntPrtclEndpntExtndd', 'ifIndex': '3', 'macAddress': '00:c8:8b:80:bb:02', 'speed': '1000000', 'adminStatus': 'UP', 'vlanId': '0', 'deviceId': '1904ca0d-01be-4d13-88e5-4f4f9980b512', 'portName': 'GigabitEthernet0/0/0', 'duplex': 'FullDuplex', 'lastUpdated': '2019-03-16 01:50:02.821', 'portMode': 'routed', 'portType': 'Ethernet Port', 'mediaType': 'T', 'series': 'Cisco ASR 1000 Series Aggregation Services Routers', 'ipv4Address': None, 'ipv4Mask': None, 'isisSupport': 'false', 'mappedPhysicalInterfaceId': None, 'mappedPhysicalInterfaceName': None, 'nativeVlanId': None, 'ospfSupport': 'false', 'pid': 'ASR1001-X', 'serialNo': 'FXS1932Q1SE', 'voiceVlan': None, 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'instanceUuid': '60f48a8a-d646-420a-a9bd-84f7a3247c85', 'id': '60f48a8a-d646-420a-a9bd-84f7a3247c85'}, {'description': '', 'status': 'down', 'interfaceType': 'Physical', 'className': 'EthrntPrtclEndpntExtndd', 'ifIndex': '4', 'macAddress': '00:c8:8b:80:bb:03', 'speed': '1000000', 'adminStatus': 'UP', 'vlanId': '0', 'deviceId': '1904ca0d-01be-4d13-88e5-4f4f9980b512', 'portName': 'GigabitEthernet0/0/1', 'duplex': 'FullDuplex', 'lastUpdated': '2019-03-16 01:50:02.821', 'portMode': 'routed', 'portType': 'Ethernet Port', 'mediaType': 'T', 'series': 'Cisco ASR 1000 Series Aggregation Services Routers', 'ipv4Address': None, 'ipv4Mask': None, 'isisSupport': 'false', 'mappedPhysicalInterfaceId': None, 'mappedPhysicalInterfaceName': None, 'nativeVlanId': None, 'ospfSupport': 'false', 'pid': 'ASR1001-X', 'serialNo': 'FXS1932Q1SE', 'voiceVlan': None, 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'instanceUuid': '31cc174a-7f4a-4384-8fb3-947dca82e106', 'id': '31cc174a-7f4a-4384-8fb3-947dca82e106'}, {'description': '', 'status': 'down', 'interfaceType': 'Physical', 'className': 'EthrntPrtclEndpntExtndd', 'ifIndex': '5', 'macAddress': '00:c8:8b:80:bb:04', 'speed': '1000000', 'adminStatus': 'UP', 'vlanId': '0', 'deviceId': '1904ca0d-01be-4d13-88e5-4f4f9980b512', 'portName': 'GigabitEthernet0/0/2', 'duplex': 'FullDuplex', 'lastUpdated': '2019-03-16 01:50:02.821', 'portMode': 'routed', 'portType': 'Ethernet Port', 'mediaType': 'T', 'series': 'Cisco ASR 1000 Series Aggregation Services Routers', 'ipv4Address': None, 'ipv4Mask': None, 'isisSupport': 'false', 'mappedPhysicalInterfaceId': None, 'mappedPhysicalInterfaceName': None, 'nativeVlanId': None, 'ospfSupport': 'false', 'pid': 'ASR1001-X', 'serialNo': 'FXS1932Q1SE', 'voiceVlan': None, 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'instanceUuid': '4febf8db-f9d0-4358-8880-cc417b52977b', 'id': '4febf8db-f9d0-4358-8880-cc417b52977b'}], 'version': '1.0'}
            responses.add(responses.GET, 'http://' + rest_cmd,
                          json=json_mock,
                          status=200)
            response = requests.get('http://' + rest_cmd)
            
        if response.status_code != 200:
            # this test should fail if any other response code received
            tc.fail('expected 200-OK actual response was ' + str(response.status_code))
        else:
            for field in response.json()['response']:
                # show the fields in this response
                print(field.keys())
        # complete
        tc.okay('complete')

    


def tc_dna_intent_api_v1_network_device_module():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDeviceModule', yaml_file='params.yaml')
    tc.okay('starting')

    rest_cmd = 'dna/intent/api/v1/network-device'
    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # execute base command so we can get a list of modules
        response = dnac.get(rest_cmd)
    else:
        json_mock = {'response': [{'type': 'Cisco ASR 1001-X Router', 'family': 'Routers', 'errorCode': 'ERROR-ENABLE-PASSWORD', 'location': None, 'role': 'BORDER ROUTER', 'lastUpdateTime': 1552701002821, 'macAddress': '00:c8:8b:80:bb:00', 'hostname': 'asr1001-x.abc.inc', 'serialNumber': 'FXS1932Q1SE', 'softwareVersion': '16.3.2', 'locationName': None, 'upTime': '34 days, 1:06:09.22', 'lastUpdated': '2019-03-16 01:50:02', 'tagCount': '0', 'inventoryStatusDetail': '<status><general code="FAILED_FEAT"/><failed_features names="79 features seem to have failed : Please check the credentials provided." code="ERROR_ENABLE_PASSWORD"/><topCause code="ERROR_ENABLE_PASSWORD"/>\n</status>', 'errorDescription': 'CLI enable password for the device could not be discovered. Please ensure correct credentials are available in global credentials or in discovery job and run discovery again. You can run the new discovery for this device alone using the discovery feature. You can also update the credentials of the device using update credentials option.', 'softwareType': 'IOS-XE', 'collectionInterval': 'Global Default', 'roleSource': 'AUTO', 'apManagerInterfaceIp': '', 'associatedWlcIp': '', 'bootDateTime': '2018-10-14 16:59:30', 'collectionStatus': 'Partial Collection Failure', 'interfaceCount': '12', 'lineCardCount': '9', 'lineCardId': '19557762-4170-42c0-b4ae-c539ee996a05, 184ddd93-2fc2-4baa-aa66-67e4e2948399, c5987ca2-3f69-4341-8cf5-00431f3add0c, ab808a88-85a0-434f-895d-7b98cd0e25fb, 1e38a03d-c5dd-46dc-8038-74e83b3da5ca, ba411ee4-6e98-4bf4-afdd-1601fcc5b9e9, 454acd43-5b66-4912-a692-bb00a9725267, d5e53e21-6e3d-4e8f-881a-ea619b133511, f4fc3497-9624-44d1-b32e-4b074706727c', 'managementIpAddress': '10.10.22.253', 'memorySize': '3819298032', 'platformId': 'ASR1001-X', 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable', 'series': 'Cisco ASR 1000 Series Aggregation Services Routers', 'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'instanceUuid': '1904ca0d-01be-4d13-88e5-4f4f9980b512', 'id': '1904ca0d-01be-4d13-88e5-4f4f9980b512'}, {'type': 'Cisco Catalyst 9300 Switch', 'family': 'Switches and Hubs', 'errorCode': None, 'location': None, 'role': 'ACCESS', 'lastUpdateTime': 1552701248479, 'macAddress': 'f8:7b:20:67:62:80', 'hostname': 'cat_9k_1.marius.x-trem.ro', 'serialNumber': 'FCW2136L0AK', 'softwareVersion': '16.6.1', 'locationName': None, 'upTime': '23 days, 10:39:07.94', 'lastUpdated': '2019-03-16 01:54:08', 'tagCount': '0', 'inventoryStatusDetail': '<status><general code="FAILED_FEAT"/><topCause code="UNKNOWN"/>\n</status>', 'errorDescription': None, 'softwareType': 'IOS-XE', 'collectionInterval': 'Global Default', 'roleSource': 'AUTO', 'apManagerInterfaceIp': '', 'associatedWlcIp': '', 'bootDateTime': '2018-10-16 10:37:51', 'collectionStatus': 'Managed', 'interfaceCount': '41', 'lineCardCount': '2', 'lineCardId': 'df065d20-8d9b-4b66-a5ed-30aab545b85b, 766f14fe-8bb6-4ac7-a58c-f456f7e2ab34', 'managementIpAddress': '10.10.22.66', 'memorySize': '889226872', 'platformId': 'C9300-24UX', 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 9300 Series Switches', 'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'instanceUuid': '1a85db61-8bf2-4717-9060-9776f42e4581', 'id': '1a85db61-8bf2-4717-9060-9776f42e4581'}, {'type': 'Cisco Catalyst 9300 Switch', 'family': 'Switches and Hubs', 'errorCode': None, 'location': None, 'role': 'ACCESS', 'lastUpdateTime': 1552700548320, 'macAddress': 'f8:7b:20:71:4d:80', 'hostname': 'cat_9k_2.marius.x-trem.ro', 'serialNumber': 'FCW2140L039', 'softwareVersion': '16.6.4a', 'locationName': None, 'upTime': '24 days, 5:57:03.56', 'lastUpdated': '2019-03-16 01:42:28', 'tagCount': '0', 'inventoryStatusDetail': '<status><general code="FAILED_FEAT"/><topCause code="UNKNOWN"/>\n</status>', 'errorDescription': None, 'softwareType': 'IOS-XE', 'collectionInterval': 'Global Default', 'roleSource': 'AUTO', 'apManagerInterfaceIp': '', 'associatedWlcIp': '', 'bootDateTime': '2018-10-16 10:37:05', 'collectionStatus': 'Managed', 'interfaceCount': '41', 'lineCardCount': '2', 'lineCardId': 'fb1bc751-e9c3-4f76-8dd6-e1f8eb125f5d, 0c8e3427-8af1-4117-a1a1-d26f62fdba57', 'managementIpAddress': '10.10.22.70', 'memorySize': '1425966824', 'platformId': 'C9300-24UX', 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 9300 Series Switches', 'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'instanceUuid': '2800864b-78ff-4bfd-9a60-83364d35c197', 'id': '2800864b-78ff-4bfd-9a60-83364d35c197'}, {'type': 'Cisco Catalyst38xx stack-able ethernet switch', 'family': 'Switches and Hubs', 'errorCode': None, 'location': None, 'role': 'DISTRIBUTION', 'lastUpdateTime': 1552700858994, 'macAddress': 'cc:d8:c1:15:d2:80', 'hostname': 'cs3850.marius.x-trem.ro', 'serialNumber': 'FOC1833X0AR', 'softwareVersion': '16.6.2s', 'locationName': None, 'upTime': '24 days, 6:05:05.68', 'lastUpdated': '2019-03-16 01:47:38', 'tagCount': '0', 'inventoryStatusDetail': '<status><general code="FAILED_FEAT"/><topCause code="UNKNOWN"/>\n</status>', 'errorDescription': None, 'softwareType': 'IOS-XE', 'collectionInterval': 'Global Default', 'roleSource': 'AUTO', 'apManagerInterfaceIp': '', 'associatedWlcIp': '', 'bootDateTime': '2018-10-16 10:40:12', 'collectionStatus': 'Managed', 'interfaceCount': '59', 'lineCardCount': '2', 'lineCardId': '529ae584-3c97-492d-bad0-a79e25be334b, a7b77de2-a3dd-400d-a826-6c1ae387a555', 'managementIpAddress': '10.10.22.73', 'memorySize': '873744896', 'platformId': 'WS-C3850-48U-E', 'reachabilityFailureReason': '', 'reachabilityStatus': 'Reachable', 'series': 'Cisco Catalyst 3850 Series Ethernet Stackable Switch', 'snmpContact': '', 'snmpLocation': '', 'tunnelUdpPort': None, 'waasDeviceMode': None, 'instanceTenantId': '5bd3634ab2bea0004c3ebb58', 'instanceUuid': '79d3a90b-1b95-4cd8-a9bd-6d5952814432', 'id': '79d3a90b-1b95-4cd8-a9bd-6d5952814432'}], 'version': '1.0'}
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)
        
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:    
        # get the unique module IDs
        module_list = []
        for device in response.json()['response']:
            for line_card in device['lineCardId'].split(', '):
                if line_card not in module_list:
                    module_list.append(line_card)

        # get information about each line card
        for module in module_list:
            rest_cmd = 'dna/intent/api/v1/network-device/module/' + module
            if not use_mock:
                response = dnac.get(rest_cmd)
            else:
                json_mock = {'response': {'name': 'module R0', 'description': 'Cisco ASR1001-X Route Processor', 'vendorEquipmentType': 'cevModuleASR1001XRP', 'assemblyNumber': '68-4703-08', 'assemblyRevision': '', 'isReportingAlarmsAllowed': 'UNKNOWN', 'serialNumber': 'JAE200306M2', 'manufacturer': 'Cisco Systems Inc', 'partNumber': 'ASR1001-X', 'entityPhysicalIndex': '7000', 'containmentEntity': '1', 'operationalStateCode': 'enabled', 'isFieldReplaceable': 'FALSE', 'id': '19557762-4170-42c0-b4ae-c539ee996a05'}, 'version': '1.0'}
                responses.add(responses.GET, 'http://' + rest_cmd,
                              json=json_mock,
                              status=200)
                response = requests.get('http://' + rest_cmd)
                
            if response.status_code != 200:
             # this test should fail if any other response code received
             tc.fail('expected 200-OK actual response was ' + str(response.status_code))
            else:
             # here are the expected fields
             print(response.json()['response'].keys())

        # complete
        tc.okay('complete')


# To use the mock you need to do two things
#
# (1) Be sure to set use_mock = True
#     For normal operation use_mock = False
#     Don't check-in the code with use_mock = True!
use_mock = True
#
# (2) Uncomment the following line to activate the responses module:
@responses.activate
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

    # # add new test cases to be run here
    tc_dna_intent_api_v1_network_device_collection_schedule_global()
    tc_dna_intent_api_v1_network_device_id_vlan()
    tc_dna_intent_api_v1_interface_network_device_range()
    tc_dna_intent_api_v1_network_device_module()


run_all_tests()
