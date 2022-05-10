#!/usr/bin/python3

import requests
import json

#Our github api general api request function

def github_api_request(owner, repo, cmd):
    request = "https://api.github.com/repos/" + owner + '/' + repo + '/' + cmd
    response = requests.get(request)
    #We always a dictionary list from json.loadstring
    dictlist = json.loads(response.text)
    print("orginal dict structure: " + str(dictlist))
    #Now convert this into an enumberated dictionary list
    #enumberate our keys
    enumdictlist = {index: value for index, value in enumerate(dictlist)}
    print("enumberated keys dict structure: " + str(enumdictlist))
    return enumdictlist


def get_json_from_enum_json_dict(jsondict, key):
    return jsondict.get(key)


def get_object_from_json(json, object_name):
    return json[object_name]


def get_value_from_json(json_object,json_key):
    return json_object[json_key]


if __name__ == "__main__":

    owner = "octocat"
    repo = "hello-World"
    cmd = "branches"
    object_name = "commit"
    json_key = "url"

    jsondict = github_api_request(owner, repo, cmd)

    for key in range(len(jsondict)):
        json = get_json_from_enum_json_dict(jsondict, key)
        #print("enumkey: " + str(key) + " json is: " + str(json))
        json_object =  get_object_from_json(json, object_name)
        print("JSON dictionary index " + str(key))
        print("JSON Object: " + str(json_object))
        json_value = get_value_from_json(json_object, json_key)
        print("JSON key: " + json_key)
        print("JSON value: " + json_value)


