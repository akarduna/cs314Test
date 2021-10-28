import csv 

with open('output.csv', mode='r') as fl:
    reader = csv.reader(fl)
    mydict = {rows[0]:rows[1] for rows in reader}
    print(mydict["26"])
