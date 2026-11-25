# GDB BABY STEP 3
<sub>{Reverse Engineering [Easy] - by LT 'syreal' Jones} </sub>
<br></br>

## Approach
Open file in ghidra, you see the constant is stored as:
```
        00401115 c7 45 fc        MOV        dword ptr [RBP + local_c],0x2262c96b
                 6b c9 62 22

```

## Solution
The bytes are 0x6b 0xc9 0x62 0x22, making academy{0x6bc96222} in the given flag format

## Flag
academy{1808359970}

## Takeaway
ghidra >> gdb again again



