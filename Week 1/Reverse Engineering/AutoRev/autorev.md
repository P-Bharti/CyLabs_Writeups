# Autorev-1 
<sub>{Reverse Engineering [Medium] - by SkrubLawd · picoCTF 2026} </sub>
<br></br>

## Approach
It turns out, though this has since been fixed since, on Ubuntu 26 Wayland terminal this program used to not detect the time between inputs, so you can take as much time as you want to copy the password the chall gives you for some reason and return it to sender

Alternatively, you can also cheese it by tee'ing the output to a file, seeing the output in vsc and copying it easily as vsc will render the binary as a single line
```
nc mysterious-sea.picoctf.net 64831 | tee data.txt
```

If you want to do it properly however, you must make a pwn _script_

You can connect to nc after importing * from pwn (via remote()), and recive (io.recvline()/.recvuntil(b"string")) and send (io.sendline(b"string")) lines from there. For some reason for me, it kept showing EOF even though it should hae worked theoretically T_T oh well.

## Solution
Fastest fingers first

## Flag
picoCTF{4u7o_r3v_g0_brrr_78c345aa}

## Takeaway
Sometimes life is unfair



