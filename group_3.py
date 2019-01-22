from utils import DnaCenter
from utils import TestCase
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

#dna/intent/api/v1/network-device
def tc_dna_intent_api_v1_network_device():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDevice', yaml_file='params.yaml')

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


def tc_dna_intent_api_v1_network_device_module():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDeviceModule', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute base command so we can get a list of modules
    response = dnac.get('dna/intent/api/v1/network-device')

    # get the unique module IDs
    module_list = []
    for device in response.json()['response']:
        for line_card in device['lineCardId'].split(', '):
            if line_card not in module_list:
                module_list.append(line_card)

    # get information about each line card
    for module in module_list:
        response = dnac.get('dna/intent/api/v1/network-device/module/' + module)
        pp.pprint(response.json())

    # complete
    tc.okay('complete')


def tc_dna_intent_api_v1_network_device_brief():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDeviceBrief', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute base command so we can get a list of device ID
    response = dnac.get('dna/intent/api/v1/network-device')

    # get the unique device IDs
    device_id_list = []
    for device in response.json()['response']:
        if device['id'] not in device_id_list:
            device_id_list.append(device['id'])
    tc.okay('found devices:' + ','.join(device_id_list))

    # get brief information about each device
    for device_id in device_id_list:
        response = dnac.get('dna/intent/api/v1/network-device/' + device_id + '/brief')
        pp.pprint(response.json())

    # complete
    tc.okay('complete')

def run_all_tests():
    # run this test case first since it will do a basic 'ping'
    tc_dna_intent_api_v1_network_device_count()

    # add new test cases to be run here
    tc_dna_intent_api_v1_network_device()
    tc_dna_intent_api_v1_network_device_module()
    tc_dna_intent_api_v1_network_device_brief()


run_all_tests()
