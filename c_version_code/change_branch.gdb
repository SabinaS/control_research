define change_branch
	b currentTempChanged
	run
	continue
	set *(char*)0x0000000000400814 = 0x74
	continue
end
document change_branch
	change bne to je
	0x74 is the code for je
end

