import fitz
import os
import hashlib

# Open PDF
pdf = fitz.open("data/chapter2.pdf")

# Create output folder
output_folder = "output/images"
os.makedirs(output_folder, exist_ok=True)

saved_hashes = set()
total_saved = 0

for page_num in range(len(pdf)):
    page = pdf.load_page(page_num)
    images = page.get_images(full=True)

    print(f"\nPage {page_num + 1}: {len(images)} images found")

    for img_index, img in enumerate(images):
        xref = img[0]

        try:
            # Extract image bytes directly
            base_image = pdf.extract_image(xref)

            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # Remove duplicate images
            image_hash = hashlib.md5(image_bytes).hexdigest()
            if image_hash in saved_hashes:
                print(f"Duplicate image skipped")
                continue

            saved_hashes.add(image_hash)

            # Save image
            filename = os.path.join(
                output_folder,
                f"page_{page_num+1}_img_{img_index}.{image_ext}"
            )

            with open(filename, "wb") as f:
                f.write(image_bytes)

            print(f"Saved: {filename}")

            total_saved += 1

        except Exception as e:
            print(f"Skipped image {img_index}: {e}")

print("\n===========================")
print(f"Total Images Saved: {total_saved}")
print("===========================")