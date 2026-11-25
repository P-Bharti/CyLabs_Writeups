# PIE TIME
<sub>{Binary Exploitation [Easy] - by Darkraicg492 · picoCTF 2025} </sub>
<br></br>

## Approach
we can find the address of main from the source bin file, then address of win wrt. to the main, subracting main address from win address we get offset, add the offset to the main address to get the flag 

## Solution
Same as approach,can use python to add/subtract hex as follows:
`python3 -c "print(hex(0x456 - 0x123))"`

## Flag
academy{b4s1c_p051t10n_1nd3p3nd3nc3_4038005c}

## Takeaway
python for hex