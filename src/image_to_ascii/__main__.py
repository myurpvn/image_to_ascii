import typer
from src.image_to_ascii.script import job

app = typer.Typer(
    name="image-to-ascii converter",
    help="A simple python app to convert images to ascii version",
    add_completion=False,
)


@app.command("")
def main():
    job()


if __name__ == "__main__":
    app()
