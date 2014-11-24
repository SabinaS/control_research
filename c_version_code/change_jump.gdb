define change_jump
	b currentTempChanged
	run
	continue
	continue
	continue
	continue
	continue
	continue
	set *(char*)0x000000000040080e = 0x74
	set *(char*)0x0000000000400847 = 0x7F
	continue
end
document change_jump
	0x74 is je
	0x7F is jg
end
