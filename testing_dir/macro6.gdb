define change_file6
b setFurnaceFanStates
run
set *(char*) 0x000000000040074e = 0x7D
si 4
continue
end

document setFurnaceFanStates
branch
end