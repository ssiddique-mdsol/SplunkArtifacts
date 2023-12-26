import yaml
import getpass
from splunklib.client import connect

class SplunkConnector:
    def __init__(self, file_path):
        """
        Initialize the SplunkConnector with a configuration file path.

        :param file_path: Path to the YAML configuration file.
        """
        self.file_path = file_path
        self.service = None

    def read_config(self, environment):
        """
        Read the Splunk configuration for a specific environment.

        :param environment: The environment to use (e.g., 'DEV').
        :return: Configuration dictionary for the specified environment.
        """
        with open(self.file_path, 'r') as file:
            config = yaml.safe_load(file)
            return config['Environments'][environment]

    def connect_to_splunk(self, environment):
        """
        Establish a connection to Splunk.

        :param environment: The environment to connect to (e.g., 'DEV').
        :return: Connected Splunk service object.
        """
        config = self.read_config(environment)

        # Get the password securely
        password = getpass.getpass(prompt="Enter your Splunk password: ")
        # Connect to Splunk
        self.service = connect(
            host=config['URL'],
            port=config['PORT'],
            username=config['User'],
            password=password
        )

        return self.service