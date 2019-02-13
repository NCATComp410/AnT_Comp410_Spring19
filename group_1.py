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
        # good sample return code check
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


def tc_dna_intent_api_vi_topology_l2_vlan():
    # create this test case
    tc = TestCase(test_name='IntentApiV1TopologyL2Vlan', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # find available vlan names
    response = dnac.get('dna/intent/api/v1/topology/vlan/vlan-names')
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code), True)

    # get additional information about each vlan
    for vlan_name in response.json()['response']:
        response = dnac.get('dna/intent/api/v1/topology/l2/' + vlan_name)
        if response.status_code != 200:
            # this test should fail if any other response code received
            tc.fail('expected 200-OK actual response was ' + str(response.status_code), True)
        else:
            pp.pprint(response.json())

    # test complete
    tc.okay('complete')


def tc_dna_intent_api_vi_topology_site_topology():
    # create this test case
    tc = TestCase(test_name='IntentApiV1SiteTopology', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # get site topology
    response = dnac.get('dna/intent/api/v1/topology/site-topology')

    # Check to see if a response other than 200-OK was received
    if response.status_code != 200:
        # this test should fail if any other response code received
        tc.fail('expected 200-OK actual response was ' + str(response.status_code), True)
    else:
        pp.pprint(response.json())

    # find unique countries
    country_list = []
    for site in response.json()['response']['sites']:
        if site['locationCountry']:
            if not site['locationCountry'] in country_list:
                country_list.append(site['locationCountry'])
    tc.okay('countries found:' + ','.join(country_list))

    # test complete
    tc.okay('complete')


def tc_dna_intent_api_vi_topology_physical_topology():
    # create this test case
    tc = TestCase(test_name='IntentApiV1PhysicalTopology', yaml_file='params.yaml')

    # create a session to the DNA-C
    dnac = DnaCenter(hostname=tc.params['DnaCenter']['Hostname'],
                     port=tc.params['DnaCenter']['Port'],
                     username=tc.params['DnaCenter']['Username'],
                     password=tc.params['DnaCenter']['Password'])

    # get physical topology
    response = dnac.get('dna/intent/api/v1/topology/physical-topology')

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
    tc_dna_intent_api_vi_topology_l2_vlan()
    tc_dna_intent_api_vi_topology_site_topology()
    tc_dna_intent_api_vi_topology_physical_topology()


run_all_tests()
