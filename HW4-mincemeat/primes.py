import mincemeat

array = range(3, 10001, 2)
bins = [[0],[1],[2],[3],[4]]
bins = [[0]]
for i in array:
    bins[i%1].append(i)
datasource = dict( (k[0], k[1:]) for k in bins)
#print datasource        

def mapfn(k, v):
    print "map"
    limit = v[len(v)-1]
    #print "limit is", limit
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if not (str(i) == str(i)[::-1]):
            #print i, " is not a palindrome"
            a[i] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            #print "yield i", i
            yield k, i
            for n in xrange(i*i, limit, i):
                a[n] = False
    #print "a is", a


def reducefn(k, x):
    #print "reduce"
    #print "k is", k, " x is", x
    #return x[0]
    return x

#print datasource
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
print "done"

