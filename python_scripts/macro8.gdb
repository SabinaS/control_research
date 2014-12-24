define change_file8
b sendNewTemp
run
set *(char*) 0x00000000004005b0 = 0x77
si 1
continue
end
document sendNewTemp
branch
end