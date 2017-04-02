import csv

with open('suspect.csv', 'rt') as csvfile:
	final_list = csv.reader(csvfile, delimiter = ',')
	for row in final_list:
		print('|'.join(row))