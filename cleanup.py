whitelisted_branches = ["test"]

def checkWhitelist(s):
    for i in whitelisted_branches:
        if (i==s):
            return True
    return False

arr = []
file = open("branches.txt", "r")
lines = file.readlines()
file.close()
with open("branches.txt") as file:
    for item in file:
        item = item.replace(' ', '')
        item = item.replace('\n', '')
        if ("DASRE-" not in item and item!="master" and checkWhitelist(item)):
            index = item.rindex("origin/") + 7
            arr.append(item[index:])
print (arr)

import subprocess
for branch in arr:
    status, commit_id = subprocess.getstatusoutput("git log master.."+branch+" --oneline | tail -1")
    print (commit_id)
    space_index = commit_id.find(' ')
    commit_id = commit_id[0:space_index]
    status, date = subprocess.getstatusoutput("git show -s --format='%ci' "+ commit_id)
    print (date)
    import datetime
    now = datetime.datetime.now()
    space_index = date.find(" +")
    date = date[0:space_index]
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    hour = int(date[11:13])
    minute = int(date[14:16])
    second = int(date[17:19])
    creation_time = datetime.datetime(year, month, day, hour, minute, second)
    delta = now - creation_time
    if (delta.days<24):
        test = subprocess.getstatusoutput("git push origin --delete " + branch)