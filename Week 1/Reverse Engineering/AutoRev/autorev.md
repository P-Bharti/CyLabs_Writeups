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

You can connect to nc after importing * from pwn (via remote()), and recive (io.recvline()/.recvuntil(b"string")) and send (io.sendline(b"string")) lines from there.

**HOWEVER**
In the midst of solving, the Chall changed _again_ and stopped leaking the password lmao.

So, what I did was run the command:
```
xxd -r -p data.txt chall
```
Where data.txt contained the binary dump

This gave me a executable that I could run after running
```
chmod u+x chall
```

But more importantly, I could open this executable in a new project in ghidra and find out the secret of the program in the if statement

(Btw, `strings chall` did not return anything useful)

Obviously this process cannot be repeated in 1 sec each, but in ghidra I was also able to see where in the binary the secret was stored

As this binary is mass produced, it should be in the same place each time as only the secret changes round to round

In listing window in ghidra we see
```
        0040113e c7 45 fc        MOV        dword ptr [RBP + local_c],0xb6788343
                 43 83 78 b6

```

Here, `c7 45 fc` is the chars we are looking for before the secret comes (`43 83 78 b6`) which are little endian signed ints for the secret

So, simply search for bytes of `c745fc`, get the next 8 chars and convert and submit the ans in int

## Solution
Fastest fingers first / use brain

## Flag
picoCTF{4u7o_r3v_g0_brrr_78c345aa}

## Takeaway
Sometimes life is unfair/ sometimes you have to use dimaag



