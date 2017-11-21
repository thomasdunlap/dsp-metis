# Hint:  use Google to find python function
from datetime import datetime

def difference_in_days(date1, date2):
    d1 = datetime.strptime(date1, '%m-%d-%Y')
    d2 = datetime.strptime(date2, '%m-%d-%Y')
    diff = datetime(d2.year, d2.month, d2.day) - datetime(d1.year, d1.month, d1.day)
    return diff.days
####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'
print('a)', difference_in_days(date_start, date_stop))
####b)
date_start = '12312013'
date_stop = '05282015'
date_start = '12-31-2013'
date_stop = '05-28-2015'
print('b)', difference_in_days(date_start, date_stop))
####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
date_start = '01-15-1994'
date_stop = '07-14-2015'
print('c)', difference_in_days(date_start, date_stop))
