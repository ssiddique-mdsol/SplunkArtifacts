import argparse
import sys
from automation.splunk_connector import SplunkConnector
from splunk_operations.pull import SplunkArtifactPuller

class SplunkAutomation:
    def __init__(self, config_path):
        self.config_path = config_path
        self.connector = SplunkConnector(config_path)

    def run(self, environment, pull_artifacts=False):
        try:
            service = self.connector.connect_to_splunk(environment)
            if pull_artifacts:
                self.pull_artifacts(service, environment)
        except FileNotFoundError:
            print("Configuration file 'environments.yml' not found.")
            sys.exit(1)
        except KeyError:
            print(f"Environment '{environment}' not found in the configuration.")
            sys.exit(1)
        except Exception as e:
            print(f"Error occurred: {e}")
            sys.exit(1)
        print("Splunk Automation tasks completed successfully.")

    def pull_artifacts(self, service, environment):
        config = self.connector.read_config(environment)
        repo_path = config['Repo']
        puller = SplunkArtifactPuller(service, repo_path)
        puller.pull_artifacts()

def main():
    parser = argparse.ArgumentParser(description='Splunk Automation Script')
    parser.add_argument('-env', '--environment', required=True, help='Environment name (e.g., DEV, PROD)')
    parser.add_argument('-pull', action='store_true', help='Pull Splunk Artifacts')
    args = parser.parse_args()

    automation = SplunkAutomation('config/environments.yml')
    automation.run(args.environment, args.pull)

if __name__ == '__main__':
    main()