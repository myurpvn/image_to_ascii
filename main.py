from PIL import Image
import os
import glob
from typing import Any
from PIL.Image import Image as ImageType


def write_to_file(file_cursor: Any, string: str) -> None:
    file_cursor.write(string)


def initial_check() -> None:
    for dir in ["images", "resized_images", "ascii_files"]:
        if not os.path.exists(dir):
            os.mkdir(dir)


def generate_ascii_file(
    image: ImageType, image_name: str, size: tuple[int, int]
) -> None:

    filepath = f"ascii_files/{image_name}.txt"

    if os.path.exists(filepath):
        os.remove(filepath)

    with open(filepath, "a+") as f:
        for i in range(size[0]):
            for j in range(size[1]):
                pixel_val = image.getpixel((j, i))
                if pixel_val in range(32):
                    write_to_file(f, "!")
                elif pixel_val in range(32, 64):
                    write_to_file(f, "@")
                elif pixel_val in range(64, 96):
                    write_to_file(f, "/")
                elif pixel_val in range(96, 128):
                    write_to_file(f, "}")
                elif pixel_val in range(128, 160):
                    write_to_file(f, "(")
                elif pixel_val in range(160, 192):
                    write_to_file(f, "|")
                elif pixel_val in range(192, 224):
                    write_to_file(f, "*")
                else:
                    write_to_file(f, "#")
            write_to_file(f, "\n")


if __name__ == "__main__":

    resize_factor = 0.25
    pattern = "Images/*"
    file_list = glob.glob(pattern)

    for image_file in file_list:
        image_name = image_file.split("/")[1]
        image = Image.open(image_file)
        w, h = image.size
        new_size = (round((w * resize_factor)), round(h * resize_factor))
        resized_image = image.resize(new_size)
        resized_image.save(f"resized_images/{image_name}.jpg")
        gray_image = resized_image.convert("L")
        generate_ascii_file(gray_image, image_name, new_size)
