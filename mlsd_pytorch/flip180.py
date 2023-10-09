from PIL import Image
import os

def flip_images_in_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(folder_path, filename)
                image = Image.open(image_path)
                flipped_image = image.transpose(Image.ROTATE_180)
                flipped_image.save(image_path)
                print(f"Flipped {filename} successfully.")
    except Exception as e:
        print("An error occurred:", e)

# 替换为你实际的文件夹路径
folder_path = "/Users/dengxinran/Desktop/Ma_thesis/DATA/020823flip180"

flip_images_in_folder(folder_path)
