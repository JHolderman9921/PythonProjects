
path_to_file = "./books/frankenstein.txt"
with open(path_to_file) as f:
    fileRead = f.read()
    print(fileRead)

print(len(fileRead.split()))
newDict = {}
newfileRead = fileRead.split()

for word in newfileRead:
    for char in word:
        try: 
            if(newDict[char.lower()] > 0):
                newDict[char.lower()] = newDict[char.lower()] + 1
            else:
                newDict[char.lower()] = 1 
        except Exception as e:
            newDict[char.lower()] = 1

for key in newDict: 
    print(f"the '{key} character was found {newDict[key]} times")