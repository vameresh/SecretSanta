import random

list1 = ["Ved", "Sydney", "Vibhanshu", "Dylan", "Liza", "Madeline"]
list2 = ["Sydney", "Ved", "Vibhanshu", "Dylan", "Liza", "Madeline"]

no_map = {}
no_map["Ved"] = "Sydney"
no_map["Sydney"] = "Ved"

def printList():
    for i in range(len(list1)):
        print(list1[i] + " ->  " + list2[i])

def writeList():
    for i in range(len(list1)):
        filename = list1[i] + ".txt"
        f = open(filename, "w")
        f.write(list2[i])
        f.close()

def invalidPair(name1, name2):
    if name1 == name2:
        return True
    elif name1 in no_map and no_map[name1] == name2:
        return True
    elif name2 in no_map and no_map[name2] == name1:
        return True
    else:
        False



satisfied = False

i = 0

while i < len(list1):
    if invalidPair(list1[i], list2[i]):
        random.shuffle(list2)
        i = 0
    i += 1

print("Successful pairing found!")
writeList()