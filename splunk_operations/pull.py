import os
import json

class SplunkArtifactPuller:
    def __init__(self, service, repo_path):
        """
        Initialize the SplunkArtifactPuller.

        :param service: Connected Splunk service object.
        :param repo_path: Path to the repository where artifacts are saved.
        """
        self.service = service
        self.repo_path = repo_path

    def save_artifact(self, content, folder_path, artifact_name):
        """
        Save an individual artifact to a file in the specified folder.

        :param content: The content of the artifact.
        :param folder_path: The path to the folder where the artifact will be saved.
        :param artifact_name: The name of the artifact.
        """
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_path = os.path.join(folder_path, f"{artifact_name}.json")
        with open(file_path, 'w') as file:
            json.dump(content, file, indent=4)

    def pull_artifacts(self):
        """
        Pull various Splunk artifacts and save them to respective folders.
        """
        artifacts = {
            "saved_searches": self.service.saved_searches
        }

        for artifact_type, artifact_collection in artifacts.items():
            folder_path = os.path.join(self.repo_path, artifact_type)
            for artifact in artifact_collection:
                self.save_artifact(artifact.content, folder_path, artifact.name)

        print(f"Artifacts have been pulled into {self.repo_path}")

