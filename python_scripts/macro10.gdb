define change_file10
b sendNewTemp
run
set $4005a0 = $4005cc
si 10
continue
end

document sendNewTemp
datareg
end