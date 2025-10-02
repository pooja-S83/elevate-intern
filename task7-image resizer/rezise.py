import os
from PIL import Image

def resize_and_convert_images(input_folder, output_folder, size=(800, 800), output_format="PNG"):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"📂 Created output folder: {output_folder}")


    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

# ignore the other then images
        if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            continue

        try:
            with Image.open(file_path) as img:
                # Resize
                resized_img = img.resize(size)

                # Convert format
                new_filename = os.path.splitext(filename)[0] + "." + output_format.lower()
                save_path = os.path.join(output_folder, new_filename)

                resized_img.save(save_path, output_format)
                print(f"✅ Saved: {save_path}")

        except Exception as e:
            print(f"⚠️ Error processing {filename}: {e}")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))   
    input_folder = os.path.join(base_dir, "input-images")   
    output_folder = os.path.join(base_dir, "output-images") 
    resize_and_convert_images(input_folder, output_folder)
