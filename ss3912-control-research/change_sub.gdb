define change_sub
	b currentTempChanged
	run
	continue
	continue
	continue
	set *(char*)0x000000000040076a = 0x01
	continue
	continue
	continue
end
document change_sub
	changed sub to add
end

