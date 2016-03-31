import mincemeat
import timeit

start_bins = timeit.default_timer()
array = range(5, 9999, 2)
bins = [[0],[1],[2],[3],[4],[5],[6]]
#bins = [[0]]
for (i, obj) in enumerate(array):
    if obj % 2 == 0:
        continue
    if obj % 3 == 0:
        continue
    if obj % 5 == 0:
        continue
    if obj % 7 == 0:
        continue
    if obj % 9 == 0:
        continue
    if obj % 11 == 0:
        continue
    if obj % 13 == 0:
        continue
    if obj % 17 == 0:
        continue
    if obj % 19 == 0:
        continue
    if obj % 23 == 0:
        continue
    bins[obj%7].append(obj)
missingValues = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23]
bins[0] = bins[0] + missingValues
datasource = dict( (k[0], k[1:]) for k in bins)
#print "datasource is", datasource
for i in range(len(bins)-1):
    print "Bin", i, "has length", len(bins[i])
elapsed_bins = timeit.default_timer() - start_bins
print "Elapsed time for creating bins is", elapsed_bins, "seconds"

##def mapfn(k, v):
##    #print "map"
##    limit = v[len(v)-1]
##    #print "limit is", limit
##    a = [True] * limit
##    a[0] = a[1] = False
##    for (i, isprime) in enumerate(a):
##        if not (str(i) == str(i)[::-1]):
##            #print i, " is not a palindrome"
##            a[i] = False
##    for (i, isprime) in enumerate(a):
##        if isprime:
##            #print "yield i", i
##            yield k, i
##            for n in xrange(i*i, limit, i):
##                a[n] = False
##    #print "a is", a
def mapfn(k, v):
    import math
    print "Start map. k is", k, "v is", v
    for obj in v:
        #print "obj is", obj
        #if obj % 2 == 0:
        #    continue
        #if obj % 3 == 0:
        #    continue
        if not (str(obj) == str(obj)[::-1]):
            continue

        #print "beginning primes checker on", obj
        sqrtObj = math.sqrt(obj)
        i = 5
        w = 2
        isPrime = True
        while i <= sqrtObj and isPrime == True:
            #print "i*i=", i*i, "=", obj, "= obj"
            if obj % i == 0:
                isPrime = False
            i += w
            w = 6 - w
            #print "end i =", i, "w =", w
        if isPrime == True:
            #print "yielding", obj
            yield k, obj


def reducefn(k, x):
    print "reduce"
    #print "k is", k, " x is", x
    #return x[0]
    return x

start_time = timeit.default_timer()

#print datasource
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
elapsed = timeit.default_timer() - start_time
print "Total time", elapsed, "seconds"
print results
print "done"

