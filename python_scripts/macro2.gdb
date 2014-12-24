define change_file2
b sendNewTemp
run
set *(char*) 0x00000000004005a0 = 0x20
si 1
continue
end

document sendNewTemp
instr
end