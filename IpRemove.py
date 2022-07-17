import os
import json
import subprocess

import requests
response_dict = "test"
urltest = "test"
idval = "test"
def IpRemove():
    log = open(r"logs\access.log","rt")
    logline = log.readlines()[-1]
    new =    str(logline.split(" ")[0])
    ban = open(r'conf\nginx.conf','rt')
    old = ban.readlines()[179].split()
    old = old[1]
    old = str(old[:-1])
    log.close()
    ban.close()
    print(old)
    print(new)
    file = open(r'conf\nginx.conf','rt')
    filedata = file.read()
    filedata = filedata.replace(old,new)
    file.close()
    file = open(r'conf\nginx.conf','w')
    file.write(filedata)

def NewPoll():
    global urltest
    headers = {
        # Already added when you pass json= but not when you pass data=
        # 'Content-Type': 'application/json',
        'X-API-Key': <api key for strawpoll.com>',
    }
    global idval
    json_data = {
        'title': 'Poll on hopping',
        'poll_options': [
            {
                'id': 'B2ZBXVaAEnJ',
                'type': 'text',
                'position': 0,
                'vote_count': 0,
                'max_votes': 0,
                'description': 'This is a description text',
                'is_write_in': False,
                'value': 'swap',
            },
            {
                'id': 'B2ZBXVaAEnJ',
                'type': 'text',
                'position': 0,
                'vote_count': 0,
                'max_votes': 0,
                'description': 'This is a description text',
                'is_write_in': False,
                'value': 'stay',
            },],
        'poll_config': {
        'is_private': False,
        'edit_vote_permissions': 'voter',
        'require_voter_names': True,
        'hide_participants' : True,
    	},

        'type': 'multiple_choice'
    }
    response = requests.post('https://api.strawpoll.com/v3/polls', headers=headers, json=json_data)
    response_dict = json.loads(response.text)
    print(response)
    for i in response_dict:
        if i == "id":
            print("key: ", i, "val: ", response_dict.get(i))
            idval = response_dict.get(i)
        if i == "url":
            print("key: ", i, "val: ", response_dict.get(i))
            url = response_dict.get(i)
            print(url)
IpRemove()

