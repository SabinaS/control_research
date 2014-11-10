define stuck_at_one
    pc
    if $argx >= 1
         set $addr = p &arg0
    end
    break
        set {int}addr = 1
    continue
end
document stuck_at_on
    Sets either oldTemp or given variable to one.
end
