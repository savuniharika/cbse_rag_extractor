import os

folder = "output/images"

for file in os.listdir(folder):
    if file.lower().endswith(".jpx"):
        os.remove(os.path.join(folder, file))
        print(f"Deleted: {file}")

print("All .jpx files deleted.")