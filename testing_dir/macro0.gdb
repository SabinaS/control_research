define change_file0
b main
run
set *(char*) 0x00000000004008a6 = 0x20
si 8
continue
end

document main
instr
end