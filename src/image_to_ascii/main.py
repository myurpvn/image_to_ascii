import typer
from src.image_to_ascii.script import job

app = typer.Typer()


@app.command("")
def main():
    job()


if __name__ == "__main__":
    app()
