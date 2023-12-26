import unittest
from unittest.mock import patch, MagicMock, mock_open
from splunk_operations.pull import SplunkArtifactPuller
import json

class TestSplunkArtifactPuller(unittest.TestCase):

    @patch('splunk_operations.pull.os.path.exists')
    @patch('splunk_operations.pull.os.makedirs')
    def test_save_artifact(self, mock_exists, mock_makedirs):
        mock_exists.return_value = False
        artifact_content = {"key": "value"}

        # Setup the SplunkArtifactPuller instance
        puller = SplunkArtifactPuller(MagicMock(), "/fake/path")

        # Use mock_open to mock file operations
        with patch('builtins.open', mock_open(), create=True) as mock_file:
            puller.save_artifact(artifact_content, "/fake/path", "test_artifact")

            # Assert that the file has been opened for writing
            mock_file.assert_called_with('/fake/path/test_artifact.json', 'w')

            # Get the file handle from the mock
            handle = mock_file()

            # Check if write method was called
            self.assertTrue(handle.write.called)

            # Check the content written to the file
            written_content = ''.join(call.args[0] for call in handle.write.call_args_list)
            expected_content = json.dumps(artifact_content, indent=4)
            self.assertEqual(written_content, expected_content)

if __name__ == '__main__':
    unittest.main()