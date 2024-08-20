import re

with open("Userinfo.txt", "r") as file:
    names = []
    passwds = []
    types = []
    
    for line in file:
        items = file.read()
        #print(items)

        regexnames = r'%([^%]+)%'
        a = re.findall(regexnames, items)
        for item in a:
            names.append(item)
        
        regexpwd = r'&([^&]+)&'
        b = re.findall(regexpwd, items)
        for item in b:
            passwds.append(item)
        
        regextype = r'\$(.*?)\$'
        c = re.findall(regextype, items)
        for item in c:
            types.append(item)
    
validlist = []
for i in range(len(names)):
    cell1 = [names[i],passwds[i],types[i]]
    validlist.append(cell1)
    
#print(validlist)

for item in validlist:
    print("Username: ", item[0], "\nPassword: ", item[1], "\nType: ", item[2],sep="")
    print(" ")