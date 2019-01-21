import yaml
import requests
from requests.auth import HTTPBasicAuth

# Disable insecure warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# basic debug print utility
# set verbose=True to enable debug messages
# set verbose=False to turn them off
verbose = False
def dbprint(msg):
    if verbose:
        print('dbprint:', end='')
        print(msg)


# Basic class to work with a DNA-C
#
# login
#
#
class DnaCenter:
    # Init the DNA-C
    def __init__(self, hostname, port, username='', password=''):
        # create the session used to interact with the DNA-C
        # http://docs.python-requests.org/en/master/user/advanced/#session-objects
        self.session = requests.session()

        # hostname and port
        self.hostname = hostname
        self.port = port

        # save the base url with the hostname and port expanded
        self.base_url = f'https://{self.hostname}:{self.port}/'

        # login to the DNA-C using the supplied credentials
        # if username/password is blank don't automatically login
        if username != '' and password != '':
            dbprint(f'login to dnac using username:{username} password:{password}')
            self.login(username, password)

    # implement basic GET method
    def get(self, url, params={}, headers={}):
        # If there are any params build into a string
        param_str = ''
        for p in params:
            param_str = param_str + '?' + p + '=' + params[p]

        # construct the get url, send it, return the result
        get_url = self.base_url + url + param_str
        dbprint('get:' + get_url)
        return self.session.get(get_url, headers=headers)


    # Login to the DNA-C and get an auth token which will be used
    # to interact for the remainder of this session
    def login(self, username, password):
        headers = {'content-type': 'application/json'}

        # build url for login command and POST it
        url = self.base_url + 'api/system/v1/auth/token'
        r = self.session.request("POST", url, auth=HTTPBasicAuth(username, password),
                                 headers=headers, verify=False)

        # throw an exception if the http response is an error
        r.raise_for_status()

        # save the auth token for future use with this session
        self.token = r.json()['Token']
        self.session.headers.update({'x-auth-token': self.token})


class TestCase:
    def __init__(self, test_name='none', yaml_file=''):
        self.name = test_name

        # Load the yaml file to read parameters needed for test
        with open(yaml_file, 'r') as f:
            self.params = yaml.load(f)

    def okay(self, message=''):
        print('PASS:' + self.name + ':' + message)

    def fail(self, message='', abort=False):
        print('FAIL:' + self.name + ':' + message)
        if abort:
            exit(-1)

    def name(self):
        return self.name






