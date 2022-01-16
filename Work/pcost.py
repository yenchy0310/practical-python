# pcost.py
#
# Exercise 1.27
################################################################
import sys

def portfolio_cost(filename):
    f = open(filename, 'rt')
    header = next(f).split(',')
    total_cost = 0
    for line in f:
        item = line.split(',')
        try:
            cost = float(item[1]) * float(item[2])
            total_cost += cost
        except ValueError:
            print("Couldn't parse", line)

    f.close()
    return total_cost
    
if len(sys.argv) == 2:
    
    filename = sys.argv[1]
else:
    filename = './Data/portfolio.csv'

# filename = './work/Data/missing.csv'
total_cost = portfolio_cost(filename)
print('Total cost', total_cost)

#################################################################

# import gzip
# f = gzip.open('./work/Data/portfolio.csv.gz', 'rt')
# for line in f:
#     print(line, end='')

##################################################################

# import csv

# f = open('./Work/Data/portfolio.csv', 'rt')
# rows = csv.reader(f)
# header = next(rows)
# total_cost = 0
# for row in rows:
#     cost = int(row[1])*float(row[2])
#     total_cost += cost
# print('Total cost', total_cost)
# f.close()

###################################################################