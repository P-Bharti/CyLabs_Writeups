# CanYouSee 
<sub>{Forensics [Easy] - by Mubarak Mikail · picoCTF 2024} </sub>
<br></br>

## Approach
Just like RED, faced with only an image as a file the first thing that pops to mind is **exiftool** 

```
exiftool ukn_reality.jpg
```

In all the information that come out, we find an unusual listing:

```
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fYjMyMDQwYjh9Cg==
```

This was the flag ecoded in base64! (very recognisable due to its signature "=" padding)

## Solution
Either decode the base64 string with dcode, cyberchef or via terminal:
```
echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fYjMyMDQwYjh9Cg==" | base64 -d
```

## Flag
picoCTF{ME74D47A_HIDD3N_b32040b8}

## Takeaway
exiftool images like its a habit



