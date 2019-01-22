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


def tc_dna_intent_api_v1_network_device_collection_schedule_global():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDeviceCollectionScheduleGlobal', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/network-device/collection-schedule/global')
    pp.pprint(response.json())

    # complete
    tc.okay('complete')


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


# dna/intent/api/v1/network-device/${id}/vlan
def tc_dna_intent_api_v1_network_device_id_vlan():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDeviceIdVlan', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    device_list = get_unique_device_id(dnac)
    tc.okay('found ' + str(len(device_list)) + ' devices:' + ','.join(device_list))

    for device_id in device_list:
        response = dnac.get('dna/intent/api/v1/network-device/' + device_id + '/vlan')
        pp.pprint(response.json())

    # complete
    tc.okay('complete')


# dna/intent/api/v1/interface/network-device/${deviceId}/${startIndex}/${recordsToReturn}
def tc_dna_intent_api_v1_interface_network_device_range():
    # create this test case
    tc = TestCase(test_name='IntentApiV1InterfaceNetworkDeviceRange', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    device_list = get_unique_device_id(dnac)
    tc.okay('found ' + str(len(device_list)) + ' devices:' + ','.join(device_list))

    # startIndex and number of records to return will need to be tested
    start_index = 1
    records_to_return = 5
    for device_id in device_list:
        response = dnac.get(f'dna/intent/api/v1/interface/network-device/{device_id}/{start_index}/{records_to_return}')
        pp.pprint(response.json())

    # complete
    tc.okay('complete')


def run_all_tests():
    # run this test case first since it will do a basic 'ping'
    tc_dna_intent_api_v1_network_device_count()

    # add new test cases to be run here
    tc_dna_intent_api_v1_network_device_collection_schedule_global()
    tc_dna_intent_api_v1_network_device_id_vlan()
    tc_dna_intent_api_v1_interface_network_device_range()


run_all_tests()
