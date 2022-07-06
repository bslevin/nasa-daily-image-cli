import typer
import time


WELCOME_ASCII = """\nAre you ready to explore...

███████╗██████╗  █████╗  ██████╗███████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝
███████╗██████╔╝███████║██║     █████╗
╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝
███████║██║     ██║  ██║╚██████╗███████╗
╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
"""

app = typer.Typer()


@app.command()
def hello():
    '''test function'''
    typer.echo(WELCOME_ASCII)
    time.sleep(2)
    name = input("Please enter your name: ")
    typer.echo(f"Hello {name}")


if __name__ == '__main__':
    app()