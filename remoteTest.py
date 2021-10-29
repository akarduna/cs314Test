import requests
import json
import urllib3
import os
import csv

urllib3.disable_warnings()
def check_file(f):
    url = "HTTPS://localhost:"
    try:
        data = json.load(f)
    except:
        print("Failed to load file")
        return
    s = []
    for i in range(1, 28):
        if i == 8:
            continue
        port = str(i).zfill(2)
        tempUrl = url +"314"+ port + "/api/" + data['requestType']
        x = requests.post(tempUrl, json=data, verify=False)
        #print(json.dumps(x.text, indent=2))
        try:
            j = x.json()
            if (j):
                dist = [str(int) for int in j["distances"]]
                s.append(dist)
                #if(len(s) != t):
                    #print(str(i).zfill(2) + ": " + ",".join(dist))
        except BaseException as err:
            print(str(i) + ": " + str(err))
    return(s)
def check_folder(path):
    teams =  {i : [] for i in range(1, 28)}
    for filename in os.listdir(path):
        fi = open(path + filename)
        if (fi):
            val = check_file(fi)
            if(val == None):
                continue
            for i in range(len(val)):
                teams[i+1] += val[i]
    return teams
path = os.getcwd()+"/student-main/tests/sprint3/"
t = check_folder(path)
w = csv.writer(open("output.csv", "w"))
for key, val in t.items():
    w.writerow([key,val])