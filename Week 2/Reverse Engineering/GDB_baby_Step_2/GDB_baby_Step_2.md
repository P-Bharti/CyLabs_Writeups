# GDB BABY STEP 2
<sub>{Reverse Engineering [Easy] - by LT 'syreal' Jones} </sub>
<br></br>

## Approach
Open file in ghidra, you see what the function is doing:
```
  local_c = 0x1e0da;
  for (local_10 = 0; local_10 < 0x25f; local_10 = local_10 + 1) {
    local_c = local_c + local_10;
  }
  return local_c;
```

## Solution
Evaluate the result in decimal, put in the correct flag format

## Flag
academy{307019}

## Takeaway
ghidra >> gdb again



