#!/usr/bin/python
	
import sys
import os
import random

# Function to write the error line based on the error name
def write_error_line(error_prob_names, file):
	to_return = "continue\n"
	if(error_prob_names == "instr"):
		if(rand_func == "sendNewTemp"):
			to_return = ("set *(char*) 0x00000000004005a0 = 0x20\n") # mov to and
		elif(rand_func == "generateTemp"):
			to_return = ("set *(char*) 0x000000000040062c = 0x20\n") # mov to and
		elif(rand_func == "outsideFactors"):
			to_return = ("set *(char*) 0x0000000000400661 = 0x1A\n") # cmp to sub
		elif(rand_func == "updateFurnaceTime"):
			to_return = ("set *(char*) 0x00000000004006ea = 0x1A\n") # pop to sub
		elif(rand_func == "updateFanTime"):
			to_return = ("set *(char*) 0x00000000004006f6 = 0x1A\n") # cmp to sub
		elif(rand_func == "setFurnaceFanStates"):
			to_return = ("set *(char*) 0x0000000000400713 = 0x20\n") # mov to and
		elif(rand_func == "currentTempChanged"):
			to_return = ("set *(char*) 0x000000000040078a = 0x20\n") # mov to and
		elif(rand_func == "main"):
			to_return = ("set *(char*) 0x00000000004008a6 = 0x20\n") # mov to and
		else:
			to_return = ("continue\n")
	elif(error_prob_names == "branch"):
		if(rand_func == "sendNewTemp"):
			to_return = ("set *(char*) 0x00000000004005b0 = 0x77\n") # jne to ja
		elif(rand_func == "generateTemp"):
			to_return = ("set *(char*) 0x0000000000400608 = 0x74\n") # jne to je
		elif(rand_func == "outsideFactors"):
			to_return = ("set *(char*) 0x0000000000400664 = 0x77\n") # jne to ja
		elif(rand_func == "updateFurnaceTime"):
			to_return = ("set *(char*) 0x00000000004006d3 = 0x77\n") # 
		elif(rand_func == "updateFanTime"):
			to_return = ("set *(char*) 0x00000000004006f9 = 0x77\n") #
		elif(rand_func == "setFurnaceFanStates"):
			to_return = ("set *(char*) 0x000000000040074e = 0x7D\n") # jne to jge 
		elif(rand_func == "currentTempChanged"):
			to_return = ("set *(char*) 0x0000000000400775 = 0x7E\n") # jg to jle
		else:
			to_return = ("continue\n")
	elif(error_prob_names == "arith"):
		if(rand_func == "sendNewTemp"):
			to_return = ("set *(char*) 0x00000000004005cc = 0x21\n") # add to and
		elif(rand_func == "generateTemp"):
			to_return = ("set *(char*) 0x0000000000400629 = 0x5A\n") # sub to pop
		elif(rand_func == "outsideFactors"):
			to_return = ("set *(char*) 0x000000000040064e = 0x1E\n") # sub to push
			to_return = ("set *(char*) 0x000000000040068a = 0x09\n") # add to or
		elif(rand_func == "updateFurnaceTime"):
			to_return = ("set *(char*) 0x00000000004006db = 0x21\n") # add to and
		elif(rand_func == "updateFanTime"):
			to_return = ("set *(char*) 0x0000000000400701 = 0x21\n") # add to and
		else:
			to_return = ("continue\n")
	elif(error_prob_names == "datareg"):
		# Walk a random number of steps
		steps = random.randint(0, 20)
		# to_return = ("si " + str(steps) + "\n")
		if(rand_func == "sendNewTemp"):
			to_return = ("set $4005a0 = $4005cc\n") 
		elif(rand_func == "generateTemp"):
			to_return = ("set $40062c = $400621\n") 
		elif(rand_func == "outsideFactors"):
			to_return = ("set $400661 = $4006be\n") 
		elif(rand_func == "updateFurnaceTime"):
			to_return = ("set $4006ea = $4006db\n") 
		elif(rand_func == "updateFanTime"):
			to_return = ("set $4006f6 = $4006f9\n") 
		elif(rand_func == "setFurnaceFanStates"):
			to_return = ("set $400713 = $40074e\n") 
		elif(rand_func == "currentTempChanged"):
			to_return = ("set $40078a = $40080e\n") 
		elif(rand_func == "main"):
			to_return = ("set $4008a6 = $400876\n") 
		else:
			to_return = ("continue\n")
	return to_return; 

# Begin		
# First open the objdump.txt file
try:
	objdump_file = open("objdump.txt", "r")
except IOError:
	print "There was an error reading from objdump.txt"
	sys.exit();

# Look for addresses 
objdump_lines = objdump_file.readlines()

# Lists to place the different function addresses into 
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
	# For each function, set a var so we know once we"ve reached its addresses 
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
	
	# Place the addresses of each function into that function"s list
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


	
# Then open the config file
try: 
	config_file = open("config.txt", "r")
	print "Opened the file to be read"
except IOError:
	print "There was an error reading from config.txt"
	sys.exit();

# Reading each line from the file
config_lines = config_file.readlines()
file_len = len(config_lines)

file_to_debug = config_lines[0]

# File config.txt contains the variables:
	# file_to_debug
	# isntr_prob
	# datamem_prob
	# datareg_prob
	# branch_prob
	# arith_prob

for item in config_lines:
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

error_probs = [instr_prob, datamem_prob, datareg_prob, branch_prob, arith_prob]
error_probs_names = ["instr", "datamem", "datareg", "branch", "arith"]
	
# Close the file
config_file.close

# Define the gdb macros
macros_to_create = 10
for x in range (0, 10):
	file_name = "macro" + str(x) + ".gdb"
	
	# Open the file
	file = open(file_name, "w+")
	file.write("define change_file" + str(x) + "\n")

	# Break at a random location (from function calls) then run
	function = ["main", "currentTempChanged", "setFurnaceFanStates", "updateFanTime","updateFurnaceTime", "outsideFactors", "generateTemp", "sendNewTemp"]
	rand_func = random.choice(function); 
	file.write("b " + rand_func + "\n")
	file.write("run\n");

	# Choose an error based on the probability
	random_error_prob = round(random.uniform(0, 1), 1)
	# print "random_error_prob" + str(random_error_prob) 
	
	# Change the program based on the error selected
	for y in range(len(error_probs)):
		random_error_prob = random_error_prob - float(error_probs[y])
		if(random_error_prob <= 0):
			# Write the error line in the macro for each chosen error
			return_error_line = write_error_line(error_probs_names[y], file)
			file.write(return_error_line)
			# print "returned error: " + return_error_line
			break

	# Walk a random number of steps
	steps = random.randint(0, 10)
	file.write("si " + str(steps) + "\n")
	
	# Read the memory location
	# TODO 

	# Continue the program
	file.write("continue\n")
	file.write("end\n\n") 

	# Write the documentation
	file.write("document " + rand_func + "\n")
	file.write(error_probs_names[y] + "\n")
	file.write("end")


# Check the output of the macros against expected output
# TODO 


