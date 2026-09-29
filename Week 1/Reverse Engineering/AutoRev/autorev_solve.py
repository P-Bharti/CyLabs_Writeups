from pwn import *

p = remote("xebec.cylabacademy.net", 23632)

for i in range(20):
    data = p.recvuntil(b"What's the secret?:")

    # find out from ghidra once, cuz all binaries are similar
    # c7 45 fc <4 bytes of the secret in little endian>
    pos = data.find(b"c745fc")

    # 3*2 chars of header then 4*2 chars of little edian encoded secret in binary form
    secret_lil_endian = data[pos + 6:pos + 14].decode()

    # basically for eg, 78 56 34 12 -> 12 34 56 78 -> convert back from hex
    secret = int(secret_lil_endian[6:8] + secret_lil_endian[4:6] + secret_lil_endian[2:4] + secret_lil_endian[0:2], 16)

    p.sendline(str(secret).encode())

p.recvuntil(b"flag: ")

print(p.recvline().decode())
