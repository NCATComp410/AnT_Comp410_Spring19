from utils import DnaCenter
from utils import TestCase
import pprint
import responses
import requests

# define a pretty-printer for diagnostics
pp = pprint.PrettyPrinter(indent=4)


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


# dna/intent/api/v1/file/namespace
def tc_dna_intent_api_v1_file_namespace():
    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespace', yaml_file='params.yaml')
    tc.okay('starting')

    rest_cmd = 'dna/intent/api/v1/file/namespace'
    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],

                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # execute the command and get response
        response = dnac.get(rest_cmd)
    else:
        json_mock = {'response': ['ivm-kgv', 'pki-trustpool', 'config', 'swimfiles', 'ejbca', 'command-runner', 'nvsfiles'], 'version': '1.0'}
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)

    if response.status_code==200:
        print("IT WORKS ")
    else:
        print("IT DOES NOT WORK")

    values = response.json()['response']

    # here are the values that need to be checked
    print(values)

    # complete
    tc.okay('complete')


def tc_dna_intent_api_v1_file_namespace_network_device_export():
    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespaceNetworkDeviceExport', yaml_file='params.yaml')
    tc.okay('starting')

    rest_cmd = 'dna/intent/api/v1/file/namespace/network_device_export'

    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # execute the command and get response
        response = dnac.get(rest_cmd)
    else:
        json_mock = {'response': [], 'version': '1.0'}
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)

    pp.pprint(response.json())

    values = response.json()['response']
    print(values)

    # complete
    tc.okay('complete')


def tc_dna_intent_api_v1_file_namespace_ivm_kgv():
    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespaceIvmKgv', yaml_file='params.yaml')
    tc.okay('starting')

    rest_cmd = 'dna/intent/api/v1/file/namespace/ivm-kgv'

    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # execute the command and get response
        response = dnac.get(rest_cmd)
    else:
        json_mock = {'response': [{'nameSpace': 'ivm-kgv', 'name': '20181219122755126_Cisco_KnownGoodValues.tar', 'downloadPath': '/file/eceb0d70-689d-47a2-ad34-bb00643b260a', 'fileSize': '17464246', 'fileFormat': 'application/x-tar', 'md5Checksum': 'b76e897b4bbf429e5a012bb265151616', 'sha1Checksum': 'eab9dc81b6bed9df1aa971b0f0159e4338af1211', 'sftpServerList': [{'sftpserverid': '7020fdf5-c3fa-4965-80d0-53badd0d5472', 'downloadurl': '/ivm-kgv/eceb0d70-689d-47a2-ad34-bb00643b260a/20181219122755126_Cisco_KnownGoodValues.tar', 'status': 'SUCCESS', 'createTimeStamp': '12/19/2018 12:29:29', 'updateTimeStamp': '12/19/2018 12:29:29', 'id': '2e4c72f3-bc40-46c6-815e-0e29418f5efe'}], 'id': 'eceb0d70-689d-47a2-ad34-bb00643b260a'}], 'version': '1.0'}
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)

    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
            print("it works ")

    #pp.pprint(response.json())

    for field in response.json()['response']:
        # here are the fields which will need to be verified
        print(field.keys())

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
    # run this test case first since it will do a basic 'ping'
    tc_dna_intent_api_v1_network_device_count()

    # add new test cases to be run here
    tc_dna_intent_api_v1_file_namespace()
    tc_dna_intent_api_v1_file_namespace_network_device_export()
    tc_dna_intent_api_v1_file_namespace_ivm_kgv()


run_all_tests()
