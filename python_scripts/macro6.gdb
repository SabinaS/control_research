define change_file6
b generateTemp
run
set *(char*) 0x000000000040062c = 0x20
si 5
continue
end
document generateTemp
instr
end