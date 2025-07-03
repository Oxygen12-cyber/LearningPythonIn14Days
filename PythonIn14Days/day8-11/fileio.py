import os 
import csv

print(os.getcwd())

with open('fileio.csv', 'a', newline = '') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(['abraham', 'jabraham@bean.com', 'indontknow'])


