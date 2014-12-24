define change_file3
b currentTempChanged
run
set *(char*) 0x0000000000400775 = 0x7E
si 9
continue
end

document currentTempChanged
branch
end