define change_file9
b updateFanTime
run
set *(char*) 0x00000000004006f6 = 0x1A
si 10
continue
end

document updateFanTime
instr
end