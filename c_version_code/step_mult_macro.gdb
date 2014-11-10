define step_mult
    set $step_mult_max = 8
    set $step_mult_count = 0

    while ($step_mult_count < $step_mult_max)
        set $step_mult_count = $step_mult_count + 1
        printf "step #%d\n", $step_mult_count
        info registers eax
	next
    end
end
document step_mult
    Steps certain random number of times through
    the source code (between 0 and 999)
end
