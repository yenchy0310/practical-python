import os

os.getcwd()
### Exercise 1.26: File Preliminaries

# with open('./Work/Data/portfolio.csv', 'rt') as f:
#     for line in f:
#         print(line, end='')

f = open('./Work/Data/portfolio.csv', 'rt')
header = next(f).split(',')
print(header)
f.close()

