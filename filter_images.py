from PIL import Image
import numpy as np
import os

folder = "output/images"

for file in os.listdir(folder):

    path = os.path.join(folder, file)

    if not (file.endswith(".png") or file.endswith(".jpg")):
        continue

    img = Image.open(path).convert("RGB")

    w, h = img.size

    # 1. Remove very small images
    if w < 120 or h < 120:
        print("Deleted small image:", file)
        os.remove(path)
        continue

    gray = img.convert("L")
    pixels = np.array(gray)

    # 2. Remove black images
    if pixels.mean() < 15:
        print("Deleted black image:", file)
        os.remove(path)
        continue

    # 3. Remove white images
    if pixels.mean() > 245:
        print("Deleted white image:", file)
        os.remove(path)
        continue

    print("Kept:", file)