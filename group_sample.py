from utils import DnaCenter
from utils import TestCase
from utils import is_valid_ipv4_address
import pprint
import responses
import requests

# define a pretty-printer for detailed diagnostics
pp = pprint.PrettyPrinter(indent=4)

# Add ability to fall-back to older API
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

    # sprint #2 - an example mock
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
    # sprint #1 - check response codes
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

    # sprint #3 example of checking for expected fields
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

    tc_dna_intent_api_v1_network_device()


run_all_tests()
