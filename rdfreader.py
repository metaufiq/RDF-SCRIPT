import rdflib

url = "http://dbpedia.org/page/Rabbit"
g=rdflib.Graph()
g.parse(url)

for s,p,o in g:
    s = s.split('/')
    p = p.split('/')
    o = o.split('/')

    print('this is subject: '+str(s[-1]))
    print('this is predicate: '+ str(p[-1]))
    print('this is object: '+ str(o[-1]))