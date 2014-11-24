define stuck_at
	b currentTempChanged
	run
	si
	si
	set $rcx = $rcx | 0x01
	continue
	continue
	continue
end	
