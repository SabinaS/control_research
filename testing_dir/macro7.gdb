define change_file7
b updateFanTime
run
set *(char*) 0x00000000004006f6 = 0x1A
si 7
continue
end

document updateFanTime
instr
end