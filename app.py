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
    formats=['%Y-%m-%d']
)


@app.command()
def welcome():
    '''Welcome function'''
    typer.echo(WELCOME_ASCII)
    time.sleep(2)
    name = input("Please enter your name: ")
    typer.echo(f"Welcome {name}, let's get started...")


@app.command()
def get_image(date: datetime = set_date):
    print('Beaming request to NASA...')
    date = str(date.date())
    url = f'{API_URL}&date={date}'
    data = requests.get(url)

    typer.echo(data.content)


if __name__ == '__main__':
    app()