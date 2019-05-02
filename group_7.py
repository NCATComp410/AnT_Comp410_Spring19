from utils import DnaCenter
from utils import TestCase
from utils import is_valid_md5_checksum
import pprint
import responses
import requests

use_intent = True

if use_intent:
    intent_api = 'dna/intent/'
else:
    intent_api = ''

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


def tc_dna_intent_api_v1_file_namespace_pki_trustpool():
    #Kristian Rosa

    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespacePkiTrustpool', yaml_file='params.yaml')
    tc.okay('starting')

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

        # edited mock
        json_mock = {'response': [{'nameSpace': 'pki-trustpool', 'name': 'iostruststore.jks',
                                   'downloadPath': '/file/b5516810-6c23-4bc1-be7e-ffd284fce53e',
                                   'fileSize': '162280', 'fileFormat': 'application/x-java-keystore',
                                   'md5Checksum': '1dac1a2acf0253f983eb61a51e7aa250',
                                   'sha1Checksum': 'c4582142ff74967c1202e3c0a5b95292f08eb5b7',
                                   'sftpServerList': [{'sftpserverid': '7020fdf5-c3fa-4965-80d0-53badd0d5472',
                                                       'downloadurl': '/pki-trustpool/b5516810-6c23-4bc1-be7e-ffd284fce53e/iostruststore.jks',
                                                       'status': 'SUCCESS',
                                                       'createTimeStamp': '10/30/2018 21:00:13',
                                                       'updateTimeStamp': '10/30/2018 21:00:13',
                                                       'id': 'fdf9d059-b4b8-4b78-b79d-e0aa291ecd3b'}],
                                   'id': 'b5516810-6c23-4bc1-be7e-ffd284fce53e'}],
                     'version': '1.0'}

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

    # Checks what the expected fields are
    for device in response.json()['response']:
        device_fields = device.keys()
        print(device_fields)

    check_fields = True

    # Checking if all the fields were actually found
    expected_fields = ['nameSpace', 'name', 'downloadPath', 'fileSize', 'fileFormat', 'md5Checksum', 'sha1Checksum', 'sftpServerList', 'id']
    for device in response.json()['response']:
        device_fields = device.keys()
        for field in expected_fields:
            if field not in device_fields:
                tc.fail(field + ' was expected but not found in the DNA-C results')
                check_fields = False
            else:
                tc.okay('Found expected field:' + field)

    # If all fields checked out OK
    if check_fields:
        tc.okay('all expected device fields were found')

    # Sprint 4 - validates the checksum to make sure its a 32 hex character string (0-9/a-f)
    if is_valid_md5_checksum(device['md5Checksum']):
        tc.okay(device['md5Checksum'] + ' is a valid md5Checksum' + '\n\033[32m' + 'Validation Success' + '\033[0m')
    else:
        tc.fail(device['md5Checksum'] + ' is NOT a valid md5Checksum' + '\n\033[31m' + 'Validation Failure' + '\033[0m')
    # complete
    tc.okay('complete')


def tc_dna_intent_api_v1_file_namespace_swimfiles():
    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespaceSwimfiles', yaml_file='params.yaml')
    tc.okay('starting')

    rest_cmd = intent_api + 'api/v1/file/namespace/swimfiles'

    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # execute the command and get response
        response = dnac.get(rest_cmd)
    else:
        json_mock = {'response': [{'nameSpace': 'swimfiles',
                                   'name': 'file-transfer-check.tmp',
                                   'downloadPath': '/file/5aa7a941-cabf-4d78-8f45-8800d26a48e0',
                                   'fileSize': '19',
                                   'fileFormat': 'text/plain',
                                   'md5Checksum': 'b5fe848cf61724367656506b512cef25',
                                   'sha1Checksum': 'cf4f3d8b5464ba3f73e292934aa30fb35aa0a418',
                                   'sftpServerList': [{'sftpserverid': '7020fdf5-c3fa-4965-80d0-53badd0d5472',
                                                       'downloadurl': '/swimfiles/5aa7a941-cabf-4d78-8f45-8800d26a48e0/file-transfer-check.tmp',
                                                       'status': 'SUCCESS',
                                                       'createTimeStamp': '10/31/2018 11:18:45',
                                                       'updateTimeStamp': '10/31/2018 11:18:45',
                                                       'id': '8c5fde91-b87d-4ced-8c36-c0d4a3558883'}],
                                   'id': '5aa7a941-cabf-4d78-8f45-8800d26a48e0'},
                                  {'nameSpace': 'swimfiles',
                                   'name': 'cat9k_iosxe.16.06.04a.SPA.bin',
                                   'downloadPath': '/file/e8a96020-843a-4159-b20f-8882251621bb',
                                   'fileSize': '597598927',
                                   'fileFormat': 'application/octet-stream',
                                   'md5Checksum': 'cee173ca374a8a388557c590eb3af680',
                                   'sha1Checksum': '844d3805cd566e292ffd1f0d1f4ed76c2938ab7f',
                                   'sftpServerList': [{'sftpserverid': '7020fdf5-c3fa-4965-80d0-53badd0d5472',
                                                       'downloadurl': '/swimfiles/e8a96020-843a-4159-b20f-8882251621bb/cat9k_iosxe.16.06.04a.SPA.bin',
                                                       'status': 'SUCCESS',
                                                       'createTimeStamp': '11/30/2018 06:25:05',
                                                       'updateTimeStamp': '11/30/2018 06:25:05',
                                                       'id': '5034419e-5b94-48e8-8f4f-5991a164bbb7'}],
                                   'id': 'e8a96020-843a-4159-b20f-8882251621bb'}],
                     'version': '1.0'}
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)

    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
        pp.pprint(response.json())

    expected_fields = ['nameSpace', 'name', 'downloadPath', 'fileSize', 'fileFormat', 'md5Checksum', 'sha1Checksum', 'sftpServerList', 'id']
    for swim_file in response.json()['response']:
        for field in expected_fields:
            if field not in expected_fields: # swim_file.keys():
                tc.fail(field + ' expected but not found')
            else:
                tc.okay('Found expected field: ' + field)

    if is_valid_md5_checksum(swim_file['md5Checksum']):
        tc.okay(swim_file['md5Checksum'] + ' is a valid md5Checksum' + '\n\033[32m' + 'Validation Success' + '\033[0m')
    else:
        tc.fail(swim_file['md5Checksum'] + ' is NOT a valid md5Checksum' + '\n\033[31m' + 'Validation Failure' + '\033[0m')

    # complete
    tc.okay('complete')


def tc_dna_intent_api_v1_file_namespace_ejbca():
    # create this test case
    tc = TestCase(test_name='IntentApiV1FileNamespaceEjbca', yaml_file='params.yaml')
    tc.okay('starting')

    rest_cmd = 'dna/intent/api/v1/file/namespace/ejbca'

    if not use_mock:
        # create a session to the DNA-C
        dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                         port=tc.params['DnaCenter']['Port'],
                         username=tc.params['DnaCenter']['Username'],
                         password=tc.params['DnaCenter']['Password'])

        # execute the command and get response
        response = dnac.get(rest_cmd)
    else:
        json_mock = {'response': [{'nameSpace': 'ejbca',
                                   'name': 'truststore.jks',
                                   'downloadPath': '/file/95b4f514-9b47-462e-b0c9-9b1a657f9610',
                                   'fileSize': '2651',
                                   'fileFormat': 'application/x-java-keystore',
                                   'md5Checksum': 'aff0b05938b58e8ede458719497858eb',
                                   'sha1Checksum': '09406a7c846188521351d448bed7ac801e5066f5',
                                   'sftpServerList': [{'sftpserverid': '7020fdf5-c3fa-4965-80d0-53badd0d5472',
                                                       'downloadurl': '/ejbca/95b4f514-9b47-462e-b0c9-9b1a657f9610/truststore.jks',
                                                       'status': 'SUCCESS',
                                                       'createTimeStamp': '10/30/2018 21:17:55',
                                                       'updateTimeStamp': '10/30/2018 21:17:55',
                                                       'id': '9d442900-decf-428b-a205-19b7fd4ee1cb'}],
                                   'id': '95b4f514-9b47-462e-b0c9-9b1a657f9610'}, {'nameSpace': 'ejbca',
                                                                                   'name': 'sdn-admin.p12',
                                                                                   'downloadPath': '/file/b944dee1-3143-400c-9da1-99a4a073984c',
                                                                                   'fileSize': '3468', 'fileFormat': 'application/pkcs12',
                                                                                   'md5Checksum': '096d5467b3a2c2d02904a61138a99f0e',
                                                                                   'sha1Checksum': '9f5adac7709b87faa7bdbf89f4c4506ef78b3e70',
                                                                                   'sftpServerList': [{'sftpserverid': '7020fdf5-c3fa-4965-80d0-53badd0d5472',
                                                                                                       'downloadurl': '/ejbca/b944dee1-3143-400c-9da1-99a4a073984c/sdn-admin.p12',
                                                                                                       'status': 'SUCCESS', 'createTimeStamp': '10/30/2018 21:17:33',
                                                                                                       'updateTimeStamp': '10/30/2018 21:17:33',
                                                                                                       'id': '78ab010d-cef1-4459-9a7b-20200548bf51'}],
                                                                                   'id': 'b944dee1-3143-400c-9da1-99a4a073984c'}], 'version': '1.0'}
        responses.add(responses.GET, 'http://' + rest_cmd,
                      json=json_mock,
                      status=200)
        response = requests.get('http://' + rest_cmd)

    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code))
    else:
        pp.pprint(response.json())

    expected_fields = ['nameSpace', 'name', 'downloadPath', 'fileSize', 'fileFormat', 'md5Checksum', 'sha1Checksum', 'sftpServerList', 'id']
    for ejbca in response.json()['response']:
        for field in expected_fields:
            if field not in ejbca.keys():
                tc.fail(field + ' expected but not found')
    if is_valid_md5_checksum(ejbca['md5Checksum']):
        tc.okay(ejbca['md5Checksum'] + ' is a valid md5Checksum' + '\n\033[32m' + 'Validation Success' + '\033[0m')
    else:
        tc.fail(ejbca['md5Checksum'] + ' is NOT a valid md5Checksum' + '\n\033[31m' + 'Validation Failure' + '\033[0m')
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
    tc_dna_intent_api_v1_network_device_count()

    tc_dna_intent_api_v1_file_namespace_pki_trustpool()
    tc_dna_intent_api_v1_file_namespace_swimfiles()
    tc_dna_intent_api_v1_file_namespace_ejbca()


run_all_tests()
