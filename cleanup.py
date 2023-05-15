arr = []
with open("branches.txt") as file:
    for item in file:
        print(item)
        item = item.replace(' ', '')
        item = item.replace('\n', '')
        if ("DASRE-" not in item and "master" not in item):
            index = item.rindex("origin/") + 7
            print (item[index:])
            print (True)
            arr.append(item[index:])
        else:
            print (False)
print (arr)

# import subprocess
# for branch in arr:
#     test = subprocess.Popen(["git", "push", "origin", "--delete", branch], stdout=subprocess.PIPE)

# import subprocess
# test = subprocess.Popen(["git", "log", "origin/DASRE-1234", "--not", "master"], stdout=subprocess.PIPE)
# output = test.communicate()[0].decode()
# print (output.index('Date:'))
# start_index = output.index('Date:')+5
# end_index = output.index('\n\n')-6
# output = output[start_index:end_index]
# output = output.replace(' ', '')
# print (output)

# import datetime
# now = datetime.datetime.now()
# creation_time = datetime.datetime(2023, 5, 12, 1, 13, 9)
# print (creation_time)
# print (type(creation_time))
# print(now)