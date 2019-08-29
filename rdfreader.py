import rdflib
import xlsxwriter
url = "http://dbpedia.org/page/Rabbit"
g=rdflib.Graph()
g.parse(url)


workbook = xlsxwriter.Workbook(r'.\Rabbit.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

worksheet.write(row, col,     'Subject')
worksheet.write(row, col + 1, 'Predicate')
worksheet.write(row, col + 2, 'Object')


row = 1
col = 0
for s,p,o in g:
    s = s.split('/')
    p = p.split('/')
    o = o.split('/')

    print('this is subject: '+str(s[-1]))
    print('this is predicate: '+ str(p[-1]))
    print('this is object: '+ str(o[-1]))

    worksheet.write(row, col,str(s[-1]))
    worksheet.write(row, col + 1, str(p[-1]))
    worksheet.write(row, col + 2, str(o[-1]))
    
    row+=1
    

workbook.close()