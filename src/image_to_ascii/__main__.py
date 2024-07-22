import typer
from typing_extensions import Annotated
from typing import List

from src.image_to_ascii.script import job
from src.image_to_ascii.logger import logger

app = typer.Typer(
    name="image-to-ascii converter",
    help="A simple python app to convert images to ascii version",
    add_completion=False,
)


@app.command("")
def main(
    height: Annotated[int, typer.Option("--height", "-h")] = None,
    width: Annotated[int, typer.Option("--width", "-w")] = None,
    resize_factor: Annotated[float, typer.Option("--resize-factor", "-rf")] = 0.25,
    file_name: Annotated[str, typer.Option("--file", "-f")] = None,
):
    logger.info(
        "Starting Script", resize_factor=resize_factor, height=height, width=width
    )
    job(resize_factor, [width, height], file_name)


if __name__ == "__main__":
    app()
