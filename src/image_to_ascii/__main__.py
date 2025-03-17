from typing import Annotated, Optional

import typer

from src.image_to_ascii.logger import logger
from src.image_to_ascii.script import job

app = typer.Typer(
    name="image-to-ascii converter",
    help="A simple python app to convert images to ascii version",
    add_completion=False,
)


@app.command("")
def main(
    height: Annotated[Optional[int], typer.Option("--height", "-h")] = None,
    width: Annotated[Optional[int], typer.Option("--width", "-w")] = None,
    resize_factor: Annotated[float, typer.Option("--resize-factor", "-rf")] = 0.25,
    file_name: Annotated[Optional[str], typer.Option("--file", "-f")] = None,
):
    new_size: tuple[int, int] = tuple()
    file: str = ""

    if width is not None and height is not None:
        new_size = (width, height)

    if file_name is not None:
        file = file_name

    logger.info(
        "Starting Script", resize_factor=resize_factor, height=height, width=width
    )
    job(resize_factor, new_size, file)


if __name__ == "__main__":
    app()
