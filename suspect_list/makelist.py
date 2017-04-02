#!/usr/bin/env Python3

import numpy as np 
import csv
def log_results(index):
	return input("What is the suspect guilty of? (Type 'end' to end list)")
i = 0
answer = []
while True:
	result = log_results(i)
	if result == 'end':
		suspect_number = np.arange(i)
		output = []
		for i in suspect_number:
			output.append(["Suspect number %i "%(i+1), "    %s"%(answer[i])])
		with open('suspect.csv','a') as csvfile:
			file_output = csv.writer(csvfile,delimiter = ',')
			file_output.writerows(output)



		break
	else:
		answer.append(result)
		i+=1






