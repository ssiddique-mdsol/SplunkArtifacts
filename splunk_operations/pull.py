import os
import json

import warnings

def save_artifact(content, folder_path, artifact_name):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, f"{artifact_name}.json")
    with open(file_path, 'w') as file:
        json.dump(content, file, indent=4)

def pull_artifacts(service, repo_path):
    artifacts = {
        "saved_searches": service.saved_searches
    }

    for artifact_type, artifact_collection in artifacts.items():
        folder_path = os.path.join(repo_path, artifact_type)
        for artifact in artifact_collection:
            save_artifact(artifact.content, folder_path, artifact.name)

    print(f"Artifacts have been pulled into {repo_path}")


def dump(obj):
  for name in dir(obj):
    e = False
    with warnings.catch_warnings():
      warnings.simplefilter("ignore")
      try:
        v = getattr(obj, name)
      except:
        e = True
      warnings.simplefilter("default")
    if not e:
      print("obj.%s = %r" % (name, v))
    else:
      print("<inaccessible property obj.%s>" % name)