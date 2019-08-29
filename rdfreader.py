import rdflib
import xlsxwriter
import sys
url = "http://dbpedia.org/page/Rabbit"
g=rdflib.Graph()
g.parse(url)


workbook = xlsxwriter.Workbook('.\Rabbit.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

worksheet.write(row, col,     'Subject')
worksheet.write(row, col + 1, 'Predicate')
worksheet.write(row, col + 2, 'Object')

for s,p,o in g:
    s = s.split('/')
    p = p.split('/')
    o = o.split('/')

    print('this is subject: '+str(s[-1]))
    print('this is predicate: '+ str(p[-1]))
    print('this is object: '+ str(o[-1]))

workbook.close()