import glob
import os

from PIL import Image
from PIL.Image import Image as ImageType
from typing_extensions import Any

from src.image_to_ascii.logger import logger


def write_to_file(file_cursor: Any, string: str) -> None:
    file_cursor.write(string)


def check_dir() -> None:
    for directory in ["images", "resized_images", "ascii_files"]:
        if not os.path.exists(directory):
            os.mkdir(directory)


def generate_ascii_file(
    image: ImageType, image_name: str, size: tuple[int, int]
) -> None:

    filepath = f"ascii_files/{image_name}.txt"

    if os.path.exists(filepath):
        os.remove(filepath)

    with open(filepath, "a+") as f:
        for y in range(size[1]):
            for x in range(size[0]):
                pixel_val = image.getpixel((x, y))
                if pixel_val in range(32):
                    write_to_file(f, "O")
                elif pixel_val in range(32, 64):
                    write_to_file(f, "<")
                elif pixel_val in range(64, 96):
                    write_to_file(f, ">")
                elif pixel_val in range(96, 128):
                    write_to_file(f, "o")
                elif pixel_val in range(128, 160):
                    write_to_file(f, "o")
                elif pixel_val in range(160, 192):
                    write_to_file(f, "<")
                elif pixel_val in range(192, 224):
                    write_to_file(f, ">")
                else:
                    write_to_file(f, "|")
            write_to_file(f, "\n")

    logger.info("Generated ASCII file", filepath=filepath)


def job(resize_factor: float, resize: tuple[int, int], file: str):

    check_dir()
    pattern = "images/*"
    file_list: list[str] = glob.glob(pattern)

    logger.info("Looping over Images directory")

    for index, image_file in enumerate(file_list):

        if file is None or file.lower() in image_file.lower():

            image_name, image_type = image_file.split("/")[1].split(".")
            logger.info(
                f"Processing image {index+1} of {len(file_list)}",
                image=image_name,
                type=image_type,
            )
            image = Image.open(image_file)
            w, h = image.size
            logger.info("Image dimensions: ", width=w, height=h)

            new_size: tuple[int, int] = tuple()
            if len(resize) != 0:
                new_size = resize
            else:
                new_size = (
                    round(w * resize_factor),
                    round(h * resize_factor),
                )

            resized_image = image.resize(new_size)
            logger.info(
                "Resized Image dimensions: ", width=new_size[0], height=new_size[1]
            )

            resized_image.save(f"resized_images/{image_name}.{image_type}")
            logger.info(
                "Saved resized image",
                filepath=f"resized_images/{image_name}.{image_type}",
            )

            gray_image = resized_image.convert("L")
            generate_ascii_file(gray_image, image_name, new_size)
