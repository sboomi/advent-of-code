import typer
import sys
import subprocess


def main(day: int = typer.Argument(..., help="Day of the month (between 1 and 25)")):
    """
    Launches an advent of code for 2021 with a specified DAY 🎄
    """
    if not (1 <= day <= 25):
        typer.echo("Error. Day must be between 1 and 25.")
        raise typer.Abort()
    typer.echo(f"Launching solution for day {day}")
    result = subprocess.run([sys.executable, f"src/day{day}.py"], capture_output=True, text=True)
    typer.echo(result.stdout)
    typer.echo(result.stderr, err=True)


if __name__ == "__main__":
    typer.run(main)
