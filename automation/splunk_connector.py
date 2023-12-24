import yaml
import getpass
from splunklib.client import connect

def read_config(file_path, environment):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
        return config['environments'][environment]

def connect_to_splunk(config):
    # Get the password securely
    password = getpass.getpass(prompt="Enter your Splunk password: ")

    # Connect to Splunk
    service = connect(
        host=config['URL'],
        port=config['PORT'],
        username=config['User'],
        password=password
    )

    return service