PLACE YOUR CODE HERE

import csv

def get_dict():
    d = {}
    reader = csv.reader(open('faculty.csv'))
    for row in reader:
        key = row[0].split()[-1]
        if key not in d:
            d[key] = [row[1:]]
        else:
            d[key].append(row[1:])
    del d['name']
    return d

def get_dict():
    '''
    d = {}
    reader = csv.reader(open('faculty.csv'))
    for row in reader:
        key = tuple(row[0].split(' '))
        d[key] = row[1:]
    del d[('name',)]
    return d
    '''
    reader = csv.reader(open('faculty.csv'))
    d = {tuple(row[0].split(' ')): row[1:] for row in reader}
    del d[('name',)]
    return d
