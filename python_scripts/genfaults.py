#!/usr/bin/python

import sys
import os
# first open the objdump.txt file
try:
	objdump_file = open('objdump.txt', "r")
except IOError:
	print "There was an error reading from objdump.txt"
	system.exit();

# Opening the config file
try: 
	config_file = open('config.txt', "r")
	print "Opened the file to be read"
except IOError:
	print "There was an error reading from config.txt"
	system.exit();

# Reading each line from the file
lines = config_file.readlines()
# print "Lines of file" + str(lines).strip('\n')
# sys.stdout.write(" ".join(str(x) for x in lines))
file_len = len(lines)

file_to_debug = lines[0]
print "file to debug " + file_to_debug



# config.txt contains the variables:
# file_to_debug
# isntr_prob
# datamem_prob
# datareg_prob
# branch_prob
# arith_prob

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

macros_to_create = 10
for x in range (0, 10):
	file_name = "macro" + str(x) + ".gdb"
	# print "file_name" + file_name

	file = open(file_name, 'w+')
	file.write("define change_file\n")
	# b at a random location (from function calls)
	# walk a random number of steps
	# read the memory location
	# change something
	file.write("b generateTemp\n")
	file.write("end\n")





