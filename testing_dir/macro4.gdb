define change_file4
b updateFurnaceTime
run
set *(char*) 0x00000000004006d3 = 0x77
si 1
continue
end

document updateFurnaceTime
branch
end