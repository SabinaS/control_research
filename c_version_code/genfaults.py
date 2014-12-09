#!/usr/bin/python

import sys
import os
import random

# First open the objdump.txt file
try:
	objdump_file = open('objdump.txt', "r")
except IOError:
	print "There was an error reading from objdump.txt"
	sys.exit();

#look for addresses 
objdump_lines = objdump_file.readlines()

# lists to place teh different function addresses into 
list_sendNewTemp = []
list_generateTemp = []
list_outsideFactors = []
list_updateFuranceTime = []
list_updateFanTime = []
list_setFurnaceFanStates = []
list_currentTempChanged = []
list_main = []

function_states = [False, False, False, False, False, False, False, False]

for item in objdump_lines:
	# for each function, set a var so we know once we've reached its addresses 
	if("<sendNewTemp>" in item):
		function_states = [True, False, False, False, False, False, False, False]
	elif("<generateTemp>" in item):
		function_states = [False, True, False, False, False, False, False, False]
	elif("<outsideFactors>" in item):
		function_states = [False, False, True, False, False, False, False, False]
	elif("<updateFurnaceTime>" in item):
		function_states = [False, False, False, True, False, False, False, False]
	elif("<updateFanTime>" in item):
		function_states = [False, False, False, False, True, False, False, False]
	elif("<setFurnaceFanStates>" in item):
		function_states = [False, False, False, False, False, True, False, False]
	elif("<currentTempChanged>" in item):
		function_states = [False, False, False, False, False, False, True, False]
	elif("<main>" in item):
		function_states = [False, False, False, False, False, False, False, True]
	
	# place the addresses of each function into that function's list
	if(function_states[0] == True):
		list_sendNewTemp.append(item)
	if(function_states[1] == True):
		list_generateTemp.append(item)
	if(function_states[2] == True):
		list_outsideFactors.append(item)
	if(function_states[3] == True):
		list_updateFuranceTime.append(item)
	if(function_states[4] == True):
		list_updateFanTime.append(item)
	if(function_states[5] == True):
		list_setFurnaceFanStates.append(item)
	if(function_states[6] == True):
		list_currentTempChanged.append(item)
	if(function_states[7] == True):
		list_main.append(item)

objdump_file.close()
	
# Then open the config file
try: 
	config_file = open('config.txt', "r")
	print "Opened the file to be read"
except IOError:
	print "There was an error reading from config.txt"
	sys.exit();

# Reading each line from the file
config_lines = config_file.readlines()
file_len = len(config_lines)

file_to_debug = config_lines[0]
# print "file to debug " + file_to_debug

# config.txt contains the variables:
	# file_to_debug
	# isntr_prob
	# datamem_prob
	# datareg_prob
	# branch_prob
	# arith_prob

for item in config_lines:
	# print item
	if("instr" in item):
		temp_instr = item.split()
		instr_prob = temp_instr[1]
	if("datamem" in item):
		temp_datamem = item.split()
		datamem_prob = temp_datamem[1]
	if("datareg" in item):
		temp_datareg = item.split()
		datareg_prob = temp_datareg[1]
	if("branch" in item):
		temp_branch = item.split()
		branch_prob = temp_branch[1]
	if("arith" in item):
		temp_arith = item.split()
		arith_prob = temp_arith[1]


	
# Close the file
config_file.close()

# Define the gdb macros
macros_to_create = 10
for x in range (0, 10):
	file_name = "macro" + str(x) + ".gdb"
	# print "file_name" + file_name

	file = open(file_name, 'w+')
	file.write("define change_file\n")
	# b at a random location (from function calls)
	function = {'main', 'currentTempChanged', 'setFurnaceFanStates', 'updateFanTime','updateFurnaceTime', 'outsideFactors', 'generateTemp', 'sendNewTemp'}
	ran_func = random.choose(function); 
	file.write("b " + ran_func)
	# walk a random number of steps
	steps = random.randint(0, 20)
	file.write("si " + str(steps))
	# read the memory location
	# change something
	file.write("b generateTemp\n")
	file.write("end\n")





