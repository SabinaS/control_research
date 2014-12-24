define change_file12
b sendNewTemp
run
set $4005a0 = $4005cc
si 0
continue
end

document sendNewTemp
datareg
end