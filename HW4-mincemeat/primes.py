import mincemeat
import timeit

start_bins = timeit.default_timer()
#array = range(23, 301, 2)
array = range(2000000, 10000000)
bins = [[0],[1],[2],[3],[4],[5],[6]]
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
    bins[obj%7] += [obj]
#missingValues = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23]
#bins[0] = bins[0] + missingValues
datasource = dict( (k[0], k[1:]) for k in bins)
#print "datasource is", datasource
elapsed_bins = timeit.default_timer() - start_bins
print "Elapsed time for creating bins is", elapsed_bins, "seconds"

def mapfn(k, v):
    import math
    #print "Start map. k is", k, "v is", v
    for vi in range(0, len(v)-1):
        if not (str(v[vi]) == str(v[vi])[::-1]):
            continue

        #print "beginning primes checker on", obj
        sqrtObj = math.sqrt(v[vi])
        i = 5
        w = 2
        isPrime = True
        while i <= sqrtObj and isPrime == True:
            #print "i*i=", i*i, "=", v[vi], "= v[vi]"
            if v[vi] % i == 0:
                isPrime = False
            i += w
            w = 6 - w
            #print "end i =", i, "w =", w
        if isPrime == True:
            #print "yielding", v[vi]
            yield k, v[vi]


def reducefn(k, x):
    #print "reduce", k
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
elapsed = timeit.default_timer() - start_bins
print "Total time", elapsed, "seconds"
#print results
totalResults = []
for iBin in results:
    for item in results[iBin]:
        totalResults.append(item)
        #print item
totalResults.sort()
print "length of results", len(totalResults)
print "sum of results", sum(totalResults)
#print totalResults
