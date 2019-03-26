from utils import DnaCenter
from utils import TestCase
import pprint
import responses
import requests

# define a pretty-printer for diagnostics
pp = pprint.PrettyPrinter(indent=4)

# This is a very basic example of a mock.  To use this mock
#
# (1) set use_mock = True
# (2) uncomment @responses.activate
#
# Be sure to change all this back or you will continue using the mock!
#
# When use_mock is set to true we won't actually communicate with the DNA-C
# Instead we'll use some previous responses.
# Mocks are useful for several reasons.  Sometimes the real DNA-C will be down
# for maintenance and you will want to make progress on your code.
# They are also useful for simulating some responses which cannot be easily
# created using the real system - such as error conditions.
use_mock = True

# Add ability to fall-back to older API
use_intent = True

if use_intent:
    intent_api = 'dna/intent/'
else:
    intent_api = ''

# Uncomment this line to use the mock this will essentially hi-jack normal requests
#library and allow us to insert our own mocked-up responses.
# @responses.activate

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

# @responses.activate
def tc_dna_intent_api_v1_topology_l3_ospf():
    # Jakeem Cofield
    # create this test case
    tc = TestCase(test_name='IntentApiV1TopologyL3Ospf', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/topology/l3/ospf')
    # pp.pprint(response.json())
    # ######################################################################
    # ###EDITS####
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
        print("The Project works")
        pp.pprint(response.json())
    # ####################################################################
    # complete
    tc.okay('complete')

@responses.activate
def tc_dna_intent_api_v1_topology_l3_isis():
    #Alexis Cooper
    # create this test case


    tc = TestCase(test_name='IntentApiV1TopologyL3Isis', yaml_file='params.yaml')


   # execute the command and get response
   # response = dnac.get('dna/intent/api/v1/topology/l3/isis')
    # pp.pprint(response.json())
    # ####################################################################

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
        json_mock = {'response': 4, 'version': '1.0'}

        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)

    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
        pp.pprint(response.json())
    # ####################################################################

    # complete
    tc.okay('complete')

@responses.activate
def tc_dna_intent_api_v1_topology_l3_static():
    # create this test case
    # Anthony Garcia
    tc = TestCase(test_name='IntentApiV1TopologyL3Static', yaml_file='params.yaml')

    # REST API command to be executed
    rest_cmd = intent_api + 'api/v1/topology/l3/static'

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
        json_mock = {'response': {'nodes': [{'deviceType': 'Cisco Catalyst 9300 Switch', 'label': 'cat_9k_2.domain.net', 'ip': '10.10.22.70', 'softwareVersion': '16.6.1', 'greyOut': True, 'nodeType': 'device', 'family': 'Switches and Hubs', 'platformId': 'C9300-24UX', 'tags': [], 'role': 'BORDER ROUTER', 'roleSource': 'MANUAL', 'customParam': {}, 'additionalInfo': {'macAddress': 'f8:7b:20:71:4d:80', 'latitude': '51.517954', 'siteid': '3c6fdc72-c755-45c8-a032-99ee3ce60fe9', 'longitude': '-0.085751'}, 'id': '3a909883-948f-47c2-8e34-65a740ab423e'}, {'deviceType': 'Cisco Catalyst 9300 Switch', 'label': 'cat_9k_1.domain.net', 'ip': '10.10.22.66', 'softwareVersion': '16.6.1', 'greyOut': True, 'nodeType': 'device', 'family': 'Switches and Hubs', 'platformId': 'C9300-24UX', 'tags': [], 'role': 'ACCESS', 'roleSource': 'AUTO', 'customParam': {}, 'additionalInfo': {'macAddress': 'f8:7b:20:67:62:80', 'latitude': '51.517954', 'siteid': '3c6fdc72-c755-45c8-a032-99ee3ce60fe9', 'longitude': '-0.085751'}, 'id': 'f783741b-3f09-432a-95d5-77ad2ed18518'}, {'deviceType': 'wired', 'label': '10.10.22.114', 'ip': '10.10.22.114', 'greyOut': True, 'nodeType': 'HOST', 'family': 'WIRED', 'role': 'HOST', 'customParam': {}, 'additionalInfo': {'macAddress': '00:1e:13:a5:b9:40'}, 'id': '47140091-fa69-4b40-9731-4fc825380d5b'}, {'deviceType': 'wired', 'label': '10.10.22.98', 'ip': '10.10.22.98', 'greyOut': True, 'nodeType': 'HOST', 'family': 'WIRED', 'role': 'HOST', 'customParam': {}, 'additionalInfo': {'macAddress': 'c8:4c:75:68:b2:c0'}, 'id': 'e3ee7a1f-7cd7-40e4-a354-65a345842e4d'}, {'deviceType': 'cloud node', 'label': 'cloud node', 'ip': 'UNKNOWN', 'softwareVersion': 'UNKNOWN', 'greyOut': True, 'nodeType': 'cloud node', 'family': 'cloud node', 'platformId': 'UNKNOWN', 'tags': ['cloud node'], 'role': 'cloud node', 'roleSource': 'AUTO', 'customParam': {}, 'id': 'a9424d4f-d19c-42c0-8ab6-a95a43008bb4'}], 'links': [{'source': '3a909883-948f-47c2-8e34-65a740ab423e', 'startPortID': '5453c235-3a1d-4d6f-83bc-5d7c61ebf38a', 'target': '47140091-fa69-4b40-9731-4fc825380d5b', 'linkStatus': 'UP', 'greyOut': True, 'additionalInfo': {}}, {'source': 'f783741b-3f09-432a-95d5-77ad2ed18518', 'startPortID': 'ae285f42-2ac1-49cf-a4c1-b2a3e81e442b', 'target': 'e3ee7a1f-7cd7-40e4-a354-65a345842e4d', 'linkStatus': 'UP', 'greyOut': True, 'additionalInfo': {}}, {'source': 'a9424d4f-d19c-42c0-8ab6-a95a43008bb4', 'target': '3a909883-948f-47c2-8e34-65a740ab423e', 'linkStatus': 'up', 'greyOut': True}]}, 'version': '1.0'}


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

        # test complete
    tc.okay('complete')


def run_all_tests():
    # run this test case first since it will do a basic 'ping'
    tc_dna_intent_api_v1_network_device_count()

    # add new test cases to be run here
    #tc_dna_intent_api_v1_topology_l3_ospf()
    tc_dna_intent_api_v1_topology_l3_isis()
    tc_dna_intent_api_v1_topology_l3_static()


run_all_tests()
