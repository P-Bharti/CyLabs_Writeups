from pwn import *

with remote("domain", 00000) as io: # hided the domain and port because i think thats good

    io.recvuntil(b"\n") # removes the welcome msg
    for i in range(20):
        secret = io.recvline()
        print(secret.decode(), "X")
        io.sendline(secret)
        io.recvuntil(b"!\n",timeout = 0.3)

    flag = io.recvline().decode()
    print(flag)

