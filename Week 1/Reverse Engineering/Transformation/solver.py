info = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽"

# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

alternating_letters = []
for i in info:
    alternating_letters.append(chr(ord(i) >> 8))
    alternating_letters.append(chr(int(bin(ord(i))[-8:],2)))


print("".join(alternating_letters))