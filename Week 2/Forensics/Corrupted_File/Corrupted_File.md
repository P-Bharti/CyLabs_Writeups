# CORRUPTED FILE 
<sub>{Forensics [Easy] - by Yahaya Meddy · CMU-Africa} </sub>
<br></br>

## Approach
view the xxd of file via `xxd file` and notice the header is wrong, where it should be `ffd8` the first few bytes are of `\x` instead; use `xxd file > image_dump.txt` then fix in text, then do `xxd -r image_dump.txt recovered.jpg`; and the flag is visible as a image

## Solution
do the commands as explained in the approach

## Flag
academy{r3st0r1ng_th3_by73s_d28873c8}

## Takeaway
xxd god


