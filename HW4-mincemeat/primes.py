import mincemeat

file = open('small.txt', 'r')
data = list(file)
file.close()

array = range(3, 201, 2)
bins = [[0],[1],[2],[3],[4]]
for i in array:
    bins[i%5].append(i)
datasource = dict( (k[0], k[1:]) for k in bins)
#print datasource

##v = [0,1,2,3,4,5,6,7,8,9,10,11,12]
##for thing in v:
##        #if palindrome
##        if (str(thing) == str(thing)[::-1]):
##            print "palindrome!", thing

#v=[3,5,7,9,11]
v = array
##a = []
##for val in v:
##    print val
##    tupl = (val, True)
##    a.append(tupl)
##print a
###a = [True] * limit
###for (i, isprime) in a:
##for (i, thing) in enumerate(a):
##    (v, isprime) = thing
##    print i, isprime
##    if isprime:
##        #yield i
##        for n in xrange(i*i, v[len(v)-1], i):
##            print "n=", n
##            a[n] = False


limit = v[len(v)-1]
print "limit is", limit
a = [True] * limit
a[0] = a[1] = False

for (i, isprime) in enumerate(a):
    if isprime:
        print "yield i", i
        for n in xrange(i*i, limit, i):     # Mark factors non-prime
            a[n] = False
for (i, isprime) in enumerate(a):
    if isprime:
        print "We have a prime", i

##def mapfn(k, v):
##    a = [True] * limit
##    a[0] = a[1] = False
##
##    for (i, isprime) in enumerate(a):
##        if isprime:
##            yield i
##            for n in xrange(i*i, limit, i):
##                a[n] = False
####    for thing in v:
####        #if palindrome
####        if (str(thing) == str(thing)[::-1]):
####            print "palindrome!", thing
####
####            #if prime
####            
####
####            yield thing, thing
##
##
##def reducefn(k, x):
##    return x
##
##
##
####def mapfn(k, v):
####    reducerNum = v % 4
####    yield v, v
####
####def reducefn(k, x):
######    print "x is ", x
######    #Is it a prime?
######    if x >= 2:
########        print "y is", y
########        return None
########        for y in range(2, x):
########            print "y is", y
########            if not ( x % y ):
########                return None
######    else:
######	return None
######    
######    #Is it a palindrome
####    
####    return x
##
##s = mincemeat.Server()
##s.datasource = datasource
##s.mapfn = mapfn
##s.reducefn = reducefn
##
##results = s.run_server(password="changeme")
##print results
##print "done"
