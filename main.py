import sys
from automation.splunk_connector import read_config, connect_to_splunk

def main():

    config = read_config('config/environments.yml', 'DEV')
    service = connect_to_splunk(config)

    try:
        service = connect_to_splunk('path_to_your_config.yml', 'DEV')
    except Exception as e:
        print(f"Error connecting to Splunk: {e}")
        sys.exit(1)

    print("Splunk Automation tasks completed successfully.")

if __name__ == '__main__':
    main()