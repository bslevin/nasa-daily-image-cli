import os
import typer
import requests
import time
from datetime import datetime
from env import API_URL

WELCOME_ASCII = """\nAre you ready to explore...

███████╗██████╗  █████╗  ██████╗███████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝
███████╗██████╔╝███████║██║     █████╗
╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝
███████║██║     ██║  ██║╚██████╗███████╗
╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
"""

app = typer.Typer()

'''set a default date variable that the NASA API can ingest
in it's required format'''
set_date = typer.Argument(
    datetime.now().strftime('%Y-%m-%d'),
    formats=['%Y-%m-%d', '']
)


def clear_terminal():
    """
    Create function to clear terminal at specific points to give the
    game a clean and clear view.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


@app.command()
def get_image(date: datetime = set_date):
    print('\nBeaming request to NASA...')
    dt = str(date)
    url = f'{API_URL}&date={dt}'
    data = requests.get(url)

    typer.echo(data.content)


@app.command()
def welcome():
    '''Welcome function'''
    typer.echo(WELCOME_ASCII)
    time.sleep(1.5)
    name = input("Please enter your name: ")
    typer.secho(
        f"Welcome {name}, let's get started...", fg=typer.colors.MAGENTA)
    time.sleep(2)

    while True:

        date_field = input(
            'Enter a date in the following format "YYYY-MM-DD"'
            "\nLeave blank and press Enter to use today's date: ")
        print(date_field)
        if date_field != '':
            get_image(date_field)
            continue
        else:
            break


welcome()


if __name__ == '__main__':
    app()