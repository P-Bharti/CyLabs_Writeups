from PIL import Image

red_file = Image.open("red.png").convert("RGBA")

diff = ""
for pixel in red_file.get_flattened_data():
    diff += str(pixel[0] & 1) + str(pixel[1] & 1) + str(pixel[2] & 1) + str(pixel[3] & 1)

bytes = [chr(int(diff[i:i+8],2)) for i in range(0,len(diff),8)]

print("".join(bytes))