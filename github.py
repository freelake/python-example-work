#!/usr/bin/python3

#github API stuff i've written

import os
import subprocess
import requests
import json


def python_version():
    cmd = "python3 --version"
    output = subprocess.check_output(cmd, shell=True)
    print("Using python version: ", output.decode("utf-8").strip())


def github_api_request(owner, repo, cmd):
    url_request = "https://api.github.com/repos/" + owner + "/" + repo + "/" + cmd
    print("request url is: " + url_request)

    response = requests.get(url_request)
    print("url response code: " + str(response.status_code))
    print(response.text)
    dictionary_list = json.loads(response.text)
    response_dict = {index: value for index, value in enumerate(dictionary_list)}
    return response_dict


def display_values_from_key_of_dict_list(dictlist, key):
    for x in range(len(dictlist)):
        jsonvalue = dictlist.get(x)
        print("dictionary: " + str(x) + " value is: " + str(jsonvalue[key]))

def display_keys_from_dict(dictname):
    print("Display keys for dict: ")
    print(str(dictname.keys()))


def display_values_from_dict(dictname):
    print("Display values for dict: ")
    print(str(dictname.values()))

if __name__ == "__main__":
    python_version()

    branches_response_dict = github_api_request("octocat", "Hello-World", "branches")

    display_keys_from_dict(branches_response_dict)
    display_values_from_dict(branches_response_dict)

    print("\nDisplay name of all branches for all keys in the dictionary.")
    display_values_from_key_of_dict_list(branches_response_dict, "name")

    print("\nDisplay commits of all branches for all keys in the dictionary.")
    display_values_from_key_of_dict_list(branches_response_dict, "commit")

    print("\nDisplay protected status of all branches for all keys in the dictionary.")
    display_values_from_key_of_dict_list(branches_response_dict, "protected")
    


