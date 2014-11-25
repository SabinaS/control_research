#!/usr/bin/python

import sys

# Opening the file
try: 
	file_object = open('config.txt', "r")
	print "Opened the file to be read"
except IOError:
	print "There was an error reading from config.txt"
	system.exit();

# Reading each line from the file
lines = file_object.readlines()
# print "Lines of file" + str(lines).strip('\n')
# sys.stdout.write(" ".join(str(x) for x in lines))
x = len(lines)

for item in lines:
	print item
	if("instr" in item):
		temp_instr = item.split()
		instr_prob = temp_instr[1]
		print instr_prob
	if("datamem" in item):
		temp_datamem = item.split()
		datamem_prob = temp_datamem[1]
		print datamem_prob
	if("datareg" in item):
		temp_datareg = item.split()
		datareg_prob = temp_datareg[1]
		print datareg_prob
	if("branch" in item):
		temp_branch = item.split()
		branch_prob = temp_branch[1]
		print branch_prob
	if("arith" in item):
		temp_arith = item.split()
		arith_prob = temp_arith[1]
		print arith_prob


	
# Close the file
file_object.close
