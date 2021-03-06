import csv
import sys
from ast import literal_eval
csv.field_size_limit(sys.maxsize)

def getList():
    reader = csv.reader(open('data.csv'), delimiter=';')
    div_list = list(reader)
    div_list.sort(key = lambda x: int(x[2]), reverse=False)
    return div_list
        
def getName(link):
    reader = csv.reader(open('data.csv'), delimiter=';')
    for row in reader:
        if row[3] == link:
            return row[0]

def getTop(num_val):
    div_list = getList()
    top_list = []
    for item in div_list[-num_val:]:
        top_list.append(item)
    top_list.sort(key = lambda x: int(x[2]), reverse=True)
    return top_list
    
