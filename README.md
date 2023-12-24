# Splunk Automation Project

## Introduction
The Splunk Automation Project is a Python-based tool designed to automate the management of various Splunk artifacts. This includes creating, updating, validating, and deploying Saved Searches, Macros, Dashboards, Reports, Event Types, and Tags. The project aims to streamline the process of managing Splunk configurations and operations, enhancing efficiency and consistency.

## Prerequisites
Before you begin, ensure you have met the following requirements:

* Python 3.6 or higher
* Access to a Splunk instance with necessary permissions
* Python packages as listed in requirements.txt

## Installation
To install the Splunk Automation Project, follow these steps:

* Clone the repository:

` git clone https://github.com/ssiddique-mdsol/SplunkArtifacts.git `

* Navigate to the project directory:

` cd splunk-automation-project`

* Install required Python packages:

`pip install -r requirements.txt`

## Configuration
Update the config/environments.yml file with your Splunk environment's details. Example configuration:

```
environments:
  DEV:
    URL: https://search-head.my-splunk.com
    PORT: 8089
    User: username@example.com
```

## Usage
To use the Splunk Automation Project, you can run the main.py script or import and use individual modules within your Python environment.

Example command to run the project:

`python main.py`

## Contributing to Splunk Automation Project
To contribute to the Splunk Automation Project, follow these steps:

* Fork this repository.
* Create a branch: git checkout -b <branch_name>.
* Make your changes and commit them: git commit -m '<commit_message>'.
* Push to the original branch: git push origin <project_name>/<location>.
* Create the pull request.


## Contributors
Thanks to the following people who have contributed to this project:

@ssiddique-mdsol

## Contact
If you want to contact me, you can reach me at ssiddique.ms@gmail.com.