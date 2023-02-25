import requests
import base64
import json
import os


class StreakHandler:
    @staticmethod
    def add_commit(user_name, repo_name, file_name, personal_access_token, commit_message, content):
        encoded_string = base64.b64encode(content.encode("ascii")).decode("ascii")
        endpoint = f"https://api.github.com/repos/{user_name}/{repo_name}/contents/{file_name}"
        headers = {
            'Authorization': f'Bearer {personal_access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.github.v3+json'
        }
        data = {
            "message": commit_message,
            "content": encoded_string
        }
        upload_response = requests.put(endpoint, headers=headers, data=json.dumps(data))
        sha = upload_response.json()["content"]["sha"]
        delete_response = requests.delete(endpoint, headers=headers, data=json.dumps({
            "message": commit_message,
            "sha": sha
        }))


if __name__ == '__main__':
    user_data = json.load(open("userdata.json", "r"))
    for user in user_data["users"]:
        user_name = user["user_name"]
        repo_name = user["repo_name"]
        file_name = user["file_name"]
        personal_access_token = user["access_token"]
        commit_message = user["commit_message"]
        content = user["file_content"]
        StreakHandler.add_commit(user_name, repo_name, file_name, personal_access_token, commit_message, content)
