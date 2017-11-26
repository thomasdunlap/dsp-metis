import csv
import re

def count_degrees(csv_file_name):
    degrees = {}
    with open(csv_file_name) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ds = row[1].split()

            for i in range(len(ds)):
                ds[i] = re.sub('\.', '', ds[i])

                ds_up = ds[i].upper()
                if ds_up not in degrees:
                    degrees[ds_up] = 1
                else:
                    degrees[ds_up] += 1

    del degrees['DEGREE']
    return degrees


import csv

def count_titles(csv_file_name):
    titles = {}
    with open(csv_file_name) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            title = line[2].split(' ')[0].lower()
            if title not in titles:
                titles[title] = 1
            else:
                titles[title] += 1

    del titles['']
    return titles


import csv

def emails(csv_file_name):
    with open(csv_file_name) as csvfile:
        reader = csv.reader(csvfile)
        return [row[3] for row in reader][1:]

def unique_domains(emails):
    return set(re.split('@', e)[1] for e in emails)
