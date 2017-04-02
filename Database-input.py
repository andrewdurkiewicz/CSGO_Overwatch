#!/usr/bin/env Python3

import numpy as np 
def log_results(index):
	return input("What is the suspect guilty of? (Type 'end' to end list)")
i = 0
answer = []
while True:
	result = log_results(i)
	if result == 'end':
		suspect_number = np.arange(i)
		for i in suspect_number:
			print("Suspect number %i:     %s"%(i+1,answer[i]))

		break
	else:
		answer.append(result)
		i+=1






