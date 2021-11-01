import requests
import json
import urllib3
import os
import csv

urllib3.disable_warnings()
def check_file(f):
    url = "https://black-bottle.cs.colostate.edu:"
    url2 = "http://localhost:8000/api/distances"
    try:
        data = json.load(f)
    except:
        print("Failed to load file")
        return
    y = requests.post(url2, json=data, verify=False)
    try:
        z = y.json()
        s = []
    except:
        return "FALSE"
    for i in range(1, 28):
        if i == 8:
            continue
        port = str(i).zfill(2)
        tempUrl = url +"314"+ port + "/api/" + data['requestType']
        x = requests.post(tempUrl, json=data, verify=False)
        #print(json.dumps(x.text, indent=2))
        try:
            j = x.json()
            if (j and j != z):
                print("diff to team: " + str(i))
        except BaseException as err:
            print(str(i) + ": " + str(err))
    return(s)
def check_folder(path):
    teams =  {i : [] for i in range(1, 28)}
    for filename in os.listdir(path):
        fi = open(path + filename)
        if (fi):
            val = check_file(fi)
    return teams
path = os.getcwd()+"/student-main/tests/sprint3/"
t = check_folder(path)

