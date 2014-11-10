define change_file
    set logging file add_output.txt
    set logging on
    set $step_mult_max = 5
    
    set $step_mult_count = 0
    while ($step_mult_count < $step_mult_max)
        set $step_mult_count = $step_mult_count + 1
        next
    end
    break
        p 'add.c'::a
        set 'add.c'::a = 1 
    continue
end
document change_file
    Walks a random number of steps through the source
    code. Then stops the program, changes one bit,
    and then continues the program. 
end
