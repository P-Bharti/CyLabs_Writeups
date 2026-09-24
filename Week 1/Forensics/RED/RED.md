# RED 
<sub>{Forensics [Easy] - by Shuailin Pan (LeConjuror) · picoCTF 2025} </sub>
<br></br>

## Approach
So, faced with only an image as a file, the first thing that pops to mind is naturally **exiftool**

```
exiftool red.png
```

In all the information that come out, we find an unusual listing:

```
Poem                            : Crimson heart, vibrant and bold,.Hearts flutter at your sight..Evenings glow softly red,.Cherries burst with sweet life..Kisses linger with your warmth..Love deep as merlot..Scarlet leaves falling softly,.Bold in every stroke.
```

The poem is deep and meaningful and totally irrelevent here. Something interesting that caught my eye was how many UpperCase Letters were present here, which hinted to a secret message

By collecting the uppercase letters we get:
```
CHECKLSB
```

Okayyyy, so what is LSB? 
LSB here stands for **Least Significant Bit** and LSB is often used to hide information in images by modifying each RGB(A) pixels by one, such that its invisible to the naked eye but can be extracted from a script

I learnt alot about this from a great [article](https://medium.com/@renantkn/lsb-steganography-hiding-a-message-in-the-pixels-of-an-image-4722a8567046) by **RenanTKN** (Check them out!)

I was already familiar with pillow from a previous cryptohack challenge, so I opted to use that method to extract the pixels.

Additionally, to get the least significant bit I masked the number with 1 (ie. NUM AND 1) to avoid manually putting 255 - i for red and modifying it to be different for other channels 

Fun stuff, I originally thought it was an RGB image, which caused me to get the wrong data extracted.. I even tried different bit lengths! 

I found out about there being the Alpha channel after doing xxd and consulting chatgpt baba about the result 🙏
```
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0080 0000 0080 0806 0000 00c3 3e61  ..............>a
```

Turns out that the second line 4th collection of numbers **0806** signifies 8 bit channels with color type 6; That denotes RGBA

## Solution
See red.py; It grabs the LSB of all 4 channels and appends them to the "diff" string, then iterates every 8 bits to form a byte and convert that into a letter

Make sure to pip install pillow in venv or globally if you dare

The result will give a repeating base64 string 
```
cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==
```

Either decode with dcode, cyberchef or via terminal:
```
echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d
```

## Flag
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}

## Takeaway
The RGB in .convert("RGB") is case sensitive gang 😔