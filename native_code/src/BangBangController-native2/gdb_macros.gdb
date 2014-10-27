# macro to walk and change BangBangController


define step_mult
    set $step_mult_max = rand() % 1000
    if $argc >= 1
        set $step_mult_max = $arg0
    end

    set $step_mult_count = 0
    while ($step_mult_count < $step_mult_max)
        set $step_mult_count = $step_mult_count + 1
        printf "step #%d\n", $step_mult_count
        step
    end
end
document step_mult
    Steps certain random number of times through
    the source code (between 0 and 999)
end

define change_file
    set $step_mult_max = rand() % 1000
    if $argc >= 1
        set $step_mult_max = $arg0
    end
    set $step_mult_count = 0
    while ($step_mult_count < $step_mult_max)
        set $step_mult_count = $step_mult_count + 1
        step
    end
    sigpause()
       set $addr = p &step
       set {int}addr = 1 
    continue
end
document change_file
    Walks a random number of steps through the source
    code. Then stops the program, changes one bit,
    and then continues the program. 
end

define stuck_at_one
    set $addr = p &oldTemp
    if $argx >= 1
         set $addr = p &arg0
    end
    sigpause()
        set {int}addr = 1
    continue
end
document stuck_at_on
    Sets either oldTemp or given variable to one.
end
define change_register
    set $mem_offset = rand() % 100
    set $addr = x/$mem_offset &main
    set $step_mult_max = rand() % 100
    if $argc >= 1
        set $step_mult_max = $arg0
        set $mem_offset = $arg0
    end
    set $step_mult_count = 0
    while ($step_mult_count < $step_mult_max)
        set $step_mult_count = $step_mult_count + 1
        step
    end
    sigpause()
        set $rand_bool = rand() %2
        set {int}addr = $rand_bool
    continue
end
document change_register
    Walk a certain number of steps. Generate a random
    offset from main to be used for re-writing memory.
    Re-write that meory location with either a 1 or 0,
    changing the value of the register. Continues.
end

define disassemble_code
    disassemble main
    end
end
document disassemble_code
    Disassemble the source code into assembler so that
    we can easily identify the instructions and memory
    registers.
end


