from utils import DnaCenter
from utils import TestCase
import pprint

# define a pretty-printer for detailed diagnostics
pp = pprint.PrettyPrinter(indent=4)


def tc_dna_intent_api_v1_network_device():
    # create this test case
    tc = TestCase(test_name='IntentApiV1NetworkDevice', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # get list of all network devices
    response = dnac.get('dna/intent/api/v1/network-device')

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
        host_list.append(device['hostname'])
        serialNumber_list.append(device['serialNumber'])

    # get list of expected host names from the parameters files
    expected_hosts = tc.params['IntentApiV1NetworkDevice']['Hosts'].split(',')
    hosts_ok = True
    for h in expected_hosts:
        # if we find an expected host that is not in the actual hosts from the reponse
        # this is a failure
        if h not in host_list:
            tc.fail(h + ' not in host_list ' + ' '.join(host_list))
            hosts_ok = False
    if hosts_ok:
        tc.okay('found all expected hosts:' + ' '.join(host_list))

    # make sure serialNumber parameter works
    sn_ok = True
    for sn in serialNumber_list:
        response = dnac.get('dna/intent/api/v1/network-device', params={'serialNumber': sn})
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
    if sn_ok:
        tc.okay('serial numbers correct')

    # try an invalid serial number
    response = dnac.get('dna/intent/api/v1/network-device', params={'serialNumber': 'invalid'})
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


def run_all_tests():
    tc_dna_intent_api_v1_network_device_count()
    tc_dna_intent_api_v1_network_device()


run_all_tests()
