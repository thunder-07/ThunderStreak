import datetime
import logging
import os
import json

import azure.functions as func
from .StreakHandler import StreakHandler


def main(mytimer: func.TimerRequest) -> None:
    user_data = json.load(open("github/userdata.json", "r"))
    for user in user_data["users"]:
        user_name = user["user_name"]
        repo_name = user["repo_name"]
        file_name = user["file_name"]
        personal_access_token = user["access_token"]
        commit_message = user["commit_message"]
        content = user["file_content"]
        StreakHandler.add_commit(user_name, repo_name, file_name, personal_access_token, commit_message, content)
