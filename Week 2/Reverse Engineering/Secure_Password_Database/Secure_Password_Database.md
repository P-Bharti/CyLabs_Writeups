# SECURE PASSWORD DATABASE
<sub>{Reverse Engineering [Easy] - by Philip Thayer - picoCTF 2026} </sub>
<br></br>

## Approach
Enter a big number like 10000000 in the terminal and see a extra list of numebers like 105 85 98 104 56 49 33 106 42 104 110 33 -86

Opening the file in ghidra, you see:
```
local_110 = calloc(0x5a,1);

for (local_118 = 0; local_118 < 0xd; local_118++) {
    local_110[local_118 + 0x3c] = obf_bytes[local_118] ^ 0xaa;
}
```

the ascii value of '\0' is 0 soo this means -86 is the xoring factor


## Solution
evalute and get the answer as 15237662580160011234, submit to the netcat

## Flag
academy{d0nt_trust_us3rs}

## Takeaway
buffer overflow goes crazy


