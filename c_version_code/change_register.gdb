define change_register
    set logging file add_output.txt
    set loggin on
    set $step_mult_max = 5
    
    set $step_mult_count = 0
    while ($step_mult_count < $step_mult_max)
        set $step_mult_count = $step_mult_count + 1
        next
    end
    break
        info registers eax
    continue
end
document change_register
    Walk a certain number of steps. Generate a random
    offset from main to be used for re-writing memory.
    Re-write that meory location with either a 1 or 0,
    changing the value of the register. Continues.
end
