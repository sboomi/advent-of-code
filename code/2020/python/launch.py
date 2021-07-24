import click


@click.command()
@click.option("--day", help="The day you want to launch")
def main(day: int):
    pass


if __name__ == "__main__":
    main()
