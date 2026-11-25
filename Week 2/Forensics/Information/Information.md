# INFORMATION 
<sub>{Forensics [Easy] - by susie · picoCTF 2021} </sub>
<br></br>

## Approach
examine metadata using `exiftool` and see that the License label was in base64

```
exiftool cat.jpg
```

## Solution
Either decode the base64 string with dcode, cyberchef or via terminal:
```
echo "YWNhZGVteXt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
```

## Flag
academy{the_m3tadata_1s_modified}

## Takeaway
base64 larp (again)



