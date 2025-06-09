from PIL import Image
import os, math, base64
path = "tiktiktik"
for folder in os.listdir(path):
	files = [base64.b64decode(f[:-4]) for f in os.listdir(f"{path}/{folder}")]
	files.sort(key=lambda x: int(x.decode().split(".")[0][6:]))
	height = width = int(math.sqrt(len(files)))
	result = Image.new("RGB", (width, height))
	i = 0
	for y in range(height):
		for x in range(width):
			if i < len(files):
				pixel = Image.open(f"{path}/{folder}/{base64.b64encode(files[i]).decode()}.png")
				result.paste(pixel, (x, y))
				i += 1
			else:
				break
	result.save(f"img_{folder}.png")