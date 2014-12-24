define change_file5
b currentTempChanged
run
set *(char*) 0x000000000040078a = 0x20
si 14
continue
end
document currentTempChanged
instr
end