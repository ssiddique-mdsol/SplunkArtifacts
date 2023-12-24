import sys
from automation.splunk_connector import read_config, connect_to_splunk

def main():

    environment = input("Enter the environment name (e.g., 'DEV', 'PROD'): ")

    try:
        config = read_config('config/environments.yml', environment)
        # Connect to Splunk with the given configuration
        service = connect_to_splunk(config)
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

if __name__ == '__main__':
    main()