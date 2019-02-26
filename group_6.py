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


# dna/intent/api/v1/file/namespace
def tc_dna_intent_api_v1_file_namespace():
    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespace', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],

                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/file/namespace')
    #pp.pprint(response.json())
    if response.status_code==200:
        print("IT WORKS ")
    else:
        print("IT DOES NOT WORK")
    # complete
    tc.okay('complete')


def tc_dna_intent_api_v1_file_namespace_network_device_export():
    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespaceNetworkDeviceExport', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/file/namespace/network_device_export')
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
     pp.pprint(response.json())

    # complete
    tc.okay('complete')


def tc_dna_intent_api_v1_file_namespace_ivm_kgv():
    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespaceIvmKgv', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/file/namespace/ivm-kgv')
    pp.pprint(response.json())

    # complete
    tc.okay('complete')


def run_all_tests():
    # run this test case first since it will do a basic 'ping'
    tc_dna_intent_api_v1_network_device_count()

    # add new test cases to be run here
    tc_dna_intent_api_v1_file_namespace()
    #tc_dna_intent_api_v1_file_namespace_network_device_export()
    #tc_dna_intent_api_v1_file_namespace_ivm_kgv()


run_all_tests()
