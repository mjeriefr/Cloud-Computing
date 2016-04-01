import mincemeat

file = open('medium.txt', 'r')
data = list(file)
file.close()

datasource = dict(enumerate(data))

def mapfn(k, v):
    for word in v.split():
        word = word.strip()
        if len(word) >= 1:
            yield "everything", word

def reducefn(k, vs):
    import math
    count = len(vs)
    
    totalSum = 0
    for item in vs:
        totalSum += int(item)

    mean = totalSum / float(count)

    variance = 0
    for item in vs:
        variance += math.pow((int(item) - mean),2)
    stdev = math.sqrt((1/float(count))*variance) #python 2.x doesn't have numpy.std
    
    return (totalSum, count, mean, stdev)

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
#print results
tupl = results['everything']
(totalSum, count, mean, stdev) = tupl
print "Sum:", totalSum, " Count", count, " Mean", mean, " Stdev", stdev
