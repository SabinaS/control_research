define change_sub_gen
	b generateTemp
	run
	continue
	continue
	continue
	set *(char*)0x00000000004005f2 = 0x01
	set *(char*)0x0000000000400610 = 0x29
	continue
	continue
	continue
end
document change_sub_gen
	changed sub to add
	and add to sub
end
