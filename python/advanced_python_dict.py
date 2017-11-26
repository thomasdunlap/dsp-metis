import csv

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
    with open('faculty.csv') as f:
        reader = csv.reader(f)
        # Dictionary (tuple of name):(rest of row) for each entry
        d = {tuple(row[0].split(' ')): row[1:] for row in reader}
        del d[('name',)]
        return d

import csv

def get_dict():
    d = {}
    with open('faculty.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            key = row[0].split()[-1]
            if key not in d:
                d[key] = [row[1:]]
            else:
                d[key].append(row[1:])
    del d['name']
    return d
