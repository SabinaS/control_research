define change_jne
	b generateTemp
	run
	continue
	set *(char*)0x0000000000400608 = 0x74
	set *(char*)0x0000000000400621 = 0x74
	continue
	continue
	continue
	continue
	continue
	continue
	continue
	continue
	continue
end
document change_jne
	jne is 75
	je is 74
end
