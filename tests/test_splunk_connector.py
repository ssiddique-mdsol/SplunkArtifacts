import unittest
from unittest.mock import patch, MagicMock
from automation.splunk_connector import SplunkConnector

class TestSplunkConnector(unittest.TestCase):

    @patch('automation.splunk_connector.connect')
    @patch('automation.splunk_connector.getpass.getpass')
    def test_connect_to_splunk_success(self, mock_getpass, mock_connect):
        # Setup
        mock_getpass.return_value = "mock_password"
        mock_connect.return_value = "Mocked Service Object"
        
        connector = SplunkConnector('config/environments.yml')
        result = connector.connect_to_splunk("DEV")

        self.assertEqual(result, "Mocked Service Object")

    @patch('automation.splunk_connector.connect')
    @patch('automation.splunk_connector.getpass.getpass')
    def test_connect_to_splunk_failure(self, mock_getpass, mock_connect):
        # Setup for failure scenario
        mock_getpass.return_value = "mock_password"
        mock_connect.side_effect = Exception("Connection failed")

        connector = SplunkConnector('config/environments.yml')

        with self.assertRaises(Exception) as context:
            connector.connect_to_splunk("DEV")

        self.assertTrue("Connection failed" in str(context.exception))

if __name__ == '__main__':
    unittest.main()