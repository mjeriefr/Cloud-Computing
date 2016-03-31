import mincemeat

file = open('small.txt', 'r')
data = list(file)
file.close()

#Assume passwords are 4 or fewer characters containing only lowercase letters and numbers.
possibleChars = "abcdefghijklmnopqrstuvwxyz0123456789"
passwordSpace = []
for char1 in list(possibleChars):
    passwordSpace.append(char1)
    for char2 in list(possibleChars):
        passwordSpace.append(char1 + char2)
        for char3 in list(possibleChars):
            passwordSpace.append(char1 + char2 + char3)
            for char4 in list(possibleChars):
                passwordSpace.append(char1 + char2 + char3 + char4)
print "created passwordSpace"

datasource = dict(enumerate(passwordSpace))

def mapfn(k, v):
    #print k, v
    #if len(v) < 4:
        #print "progress:", v
    import hashlib
    vHashed = hashlib.md5(str(v)).hexdigest()
    five = vHashed[:5]
    if five == "d077f" or five == "0832c" or five == "1a1dc" or five == "ee269" or five == "0fe63":
        print v, "-->", five
        yield v, five
    #else:
        #print v, "-//->", five

def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
