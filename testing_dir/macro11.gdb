define change_file11
b setFurnaceFanStates
run
set *(char*) 0x0000000000400713 = 0x20
si 7
continue
end

document setFurnaceFanStates
instr
end