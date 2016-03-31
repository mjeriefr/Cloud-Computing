import mincemeat
import sys
import timeit

start_time = timeit.default_timer()

#Assume passwords are 4 or fewer characters containing only lowercase letters and numbers.
possibleChars = "abcdefghijklmnopqrstuvwxyz0123456789"
passwordSpace = []
passwordSpace3 = []
for char1 in list(possibleChars):
    passwordSpace.append(char1)
    for char2 in list(possibleChars):
        passwordSpace.append(char1 + char2)
        for char3 in list(possibleChars):
            passwordSpace.append(char1 + char2 + char3)
            #passwordSpace3.append(char1 + char2 + char3)
            for char4 in list(possibleChars):
                passwordSpace.append(char1 + char2 + char3 + char4)

#user input
userInputHash = sys.argv[1]
passwordInputDoubleSpace = []
for i in range(0, len(passwordSpace)-1):
    passwordInputDoubleSpace.append([userInputHash, passwordSpace[i]])
##binsDict = {}
##for firstThreeChars in passwordSpace3:
##    binsDict[firstThreeChars] = [

#datasource = dict(enumerate(passwordSpace))
datasource = dict(enumerate(passwordInputDoubleSpace))

def mapfn(k, v):
    #print k, v
    if len(v[1]) < 2:
        print "progress:", v
    import hashlib
    vHashed = hashlib.md5(str(v[1])).hexdigest()
    #five = vHashed[:5]
    #if five == "d077f" or five == "0832c" or five == "1a1dc" or five == "ee269" or five == "0fe63":
    if vHashed[:5] == v[0]:
        print v[1], "-->", vHashed[:5]
        yield vHashed[:5], v[1]
    #else:
        #print v, "-//->", vHashed[:5]

def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = datasource
#s.conf.set("inputHash", userInputHash)
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
print "Time elapsed", (timeit.default_timer() - start_time)
