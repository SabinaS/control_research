define change_file4
b updateFurnaceTime
run
set *(char*) 0x00000000004006ea = 0x1A
si 6
continue
end
document updateFurnaceTime
instr
end