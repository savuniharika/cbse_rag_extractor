from PIL import Image
import os

input_folder = "output/images"

for file in os.listdir(input_folder):
    if file.lower().endswith(".jpx"):
        path = os.path.join(input_folder, file)

        try:
            img = Image.open(path)

            # Convert CMYK or other modes to RGB
            if img.mode != "RGB":
                img = img.convert("RGB")

            new_name = file.replace(".jpx", ".png")
            new_path = os.path.join(input_folder, new_name)

            img.save(new_path, "PNG")

            print(f"Converted: {new_name}")

        except Exception as e:
            print(f"Could not convert {file}: {e}")