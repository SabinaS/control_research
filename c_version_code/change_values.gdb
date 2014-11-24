define change_values
	b main
	run
	si
	si
	si
	si
	si
	si
	set $rdi = $rdi | 0x0000000010000 
	continue
end
