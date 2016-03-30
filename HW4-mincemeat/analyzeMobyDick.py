import mincemeat

file = open('small.txt', 'r')
data = list(file)
file.close()

datasource = dict(enumerate(data))

def mapfn(k, v):
    for word in v.split():
        print "word is ", word
        word = word.strip()
        if len(word) >= 1:
            yield word, 1

def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
