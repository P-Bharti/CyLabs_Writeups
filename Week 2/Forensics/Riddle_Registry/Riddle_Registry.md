# RIDDLE REGISTRY 
<sub>{Forensics [Easy] - by Prince Niyonshuti N · picoMini by CMU-Africa} </sub>
<br></br>

## Approach
copy pasting text can get you to see the text under the black bar, but the flag isnt there, so examine metadata using `exiftool` and see that the Author label was in base64

```
exiftool confidential.pdf
```

## Solution
Either decode the base64 string with dcode, cyberchef or via terminal:
```
echo "YWNhZGVteXtwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV85ZDNjYzY2OX0=" | base64 -d
```

## Flag
academy{puzzl3d_m3tadata_f0und!_9d3cc669}

## Takeaway
base64 larp



