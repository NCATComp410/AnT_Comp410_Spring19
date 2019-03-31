from utils import DnaCenter
from utils import TestCase
import pprint
import responses
import requests

use_intent = True

if use_intent:
    intent_api = 'dna/intent/'
else:
    intent_api = ''

use_mock = True



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

@responses.activate

def tc_dna_intent_api_v1_file_namespace_pki_trustpool():
    #Kristian Rosa

    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespacePkiTrustpool', yaml_file='params.yaml')

    # execute the command and get response
    #response = dnac.get('dna/intent/api/v1/file/namespace/pki-trustpool')

    # REST API command to be executed
    rest_cmd = intent_api + 'api/v1/file/namespace/pki-trustpool'

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

        #edited mock
        json_mock = {'response': [{'type': 'TESTING', 'location': 'DTEST'}], 'version': 2.3,}

        # instead of actually talking to the DNA-C we're going to mock-up the response
        # this command inserts our mock-up which will be retrieved by response as though it was real
        # try changing the response code to something other than 200 to test out that part of the code
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)

    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
        pp.pprint(response.json())

    check_fields = True
    expected_fields = []
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

    # complete
    tc.okay('complete')


def tc_dna_intent_api_v1_file_namespace_swimfiles():
    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespaceSwimfiles', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/file/namespace/swimfiles')
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
        pp.pprint(response.json())

    # complete
    tc.okay('complete')


def tc_dna_intent_api_v1_file_namespace_ejbca():
    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespaceEjbca', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # execute the command and get response
    response = dnac.get('dna/intent/api/v1/file/namespace/ejbca')
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
        pp.pprint(response.json())

    # complete
    tc.okay('complete')


def run_all_tests():
    # run this test case first since it will do a basic 'ping'
    tc_dna_intent_api_v1_network_device_count()

    # add new test cases to be run here
    tc_dna_intent_api_v1_file_namespace_pki_trustpool()
    tc_dna_intent_api_v1_file_namespace_swimfiles()
    tc_dna_intent_api_v1_file_namespace_ejbca()


run_all_tests()
