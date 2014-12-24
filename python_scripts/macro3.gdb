define change_file3
b sendNewTemp
run
set *(char*) 0x00000000004005a0 = 0x20
si 16
continue
end
document sendNewTemp
instr
end