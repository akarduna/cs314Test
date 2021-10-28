import requests
import json
import urllib3
import os

urllib3.disable_warnings()
def check_file(f):
    url = "https://black-bottle.cs.colostate.edu:"
    try:
        data = json.load(f)
    except:
        print("Failed to load file")
        return
    s = set()
    for i in range(1, 28):
        if i == 8:
            continue
        port = str(i).zfill(2)
        tempUrl = url +"314"+ port + "/api/distances"
        x = requests.post(tempUrl, json=data, verify=False)
        #print(json.dumps(x.text, indent=2))
        try:
            j = x.json()
            if (j):
                dist = [str(int) for int in j["distances"]]
                t = len(s)
                s.add(",".join(dist))
                if(len(s) != t):
                    print(str(i).zfill(2) + ": " + ",".join(dist))
        except BaseException as err:
            print(str(i) + ": " + str(err))
    return(s)
path = os.getcwd()+"/student-main/tests/sprint3/"
for filename in os.listdir(os.getcwd()+"/student-main/tests/sprint3/"):
    break;
    fi = open(path + filename)
    if(fi):
        val = check_file(fi)
        if(val != 1 and val != None):
            print(filename + ": " + str(val))
fi = open(path + "bilprice-4.json")
print(check_file(fi))
