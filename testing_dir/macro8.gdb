define change_file8
b currentTempChanged
run
set $40078a = $40080e
si 6
continue
end

document currentTempChanged
datareg
end