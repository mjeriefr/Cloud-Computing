import mincemeat

file = open('small.txt', 'r')
data = list(file)
file.close()

datasource = dict((i, i+1) for i in range(2, 100))
#datasource = dict((i, i+1) for i in range(2000000, 10000000))
#datasource = dict(enumerate(data))

def mapfn(k, v):
    reducerNum = v % 4
    yield v, v

def reducefn(k, x):
    print "x is ", x
    #Is it a prime?
    if x >= 2:
##        print "y is", y
##        return None
##        for y in range(2, x):
##            print "y is", y
##            if not ( x % y ):
##                return None
    else:
	return None
    
    #Is it a palindrome
    
    return x

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
print "done"
