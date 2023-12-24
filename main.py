import argparse
import sys
from automation.splunk_connector import read_config, connect_to_splunk
from splunk_operations.pull import pull_artifacts

def main():
    parser = argparse.ArgumentParser(description='Splunk Automation Script')
    parser.add_argument('-env', '--environment', required=True, help='Environment name (e.g., DEV, PROD)')
    parser.add_argument('-pull', action='store_true', help='Pull Splunk Artifacts')
    args = parser.parse_args()

    try:
        config = read_config('config/environments.yml', args.environment)
        print(config)
        service = connect_to_splunk(config)

    except FileNotFoundError:
        print("Configuration file 'environments.yml' not found.")
        sys.exit(1)
    except KeyError:
        print(f"Environment '{args.environment}' not found in the configuration.")
        sys.exit(1)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

    if args.pull:
        repo_path = config['Repo']
        pull_artifacts(service, repo_path)

    print("Splunk Automation tasks completed successfully.")

if __name__ == '__main__':
    main()