import subprocess
import sys
from pathlib import Path
from typing import Optional

import pytest
import typer

ROOT_FOLDER = Path(__file__).resolve().parents[1]
SCRIPTS_FOLDER = Path(__file__).resolve().parent / "solutions"

app = typer.Typer()


@app.callback()
def callback():
    """
    🎄🎄 Advent of Code 2022 🎄🎄
    """


@app.command()
def launch(day: int = typer.Argument(..., help="Day of the month (between 1 and 25)")):
    """
    Launches an advent of code for 2022 with a specified DAY 🎄
    """
    if not (1 <= day <= 25):
        typer.echo("Error. Day must be between 1 and 25.")
        raise typer.Abort()
    typer.echo(f"Launching solution for day {day}")
    result = subprocess.run(
        [sys.executable, (SCRIPTS_FOLDER / f"day{day}.py").as_posix()],
        capture_output=True,
        text=True,
    )
    typer.echo(result.stdout)
    typer.echo(result.stderr, err=True)


@app.command()
def test(
    day: Optional[int] = typer.Argument(
        None, help="Day of the month (between 1 and 25)"
    ),
    all_tests: bool = typer.Option(False, "--all", help="Runs every test at once"),
):
    """
    Launches suite tests against a day or every day at once
    """
    if all_tests:
        typer.echo("Running full test suite")
        pytest.main(["-vv"])

    elif day:
        if not (1 <= day <= 25):
            typer.echo("Error. Day must be between 1 and 25.")
            raise typer.Abort()

        typer.echo(f"Launching solution for day {day}")
        pytest.main([f"tests/test_day{day}.py"])

    else:
        typer.echo("Must pass at least a day (between 1 and 25)")
        raise typer.Abort()
