import pytest
from ac2023python.day_3_gear_ratios import (
    register_numbers,
    get_engine_schematic,
    Number,
    find_part_numbers,
)

EXAMPLE_INPUT = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    txt = "\n".join(EXAMPLE_INPUT)
    fn = tmp_path_factory.mktemp("data") / "day3"
    with open(fn, "w") as f:
        f.write(txt)
    return fn


def test_register_numbers(text_file):
    engine_schematic = get_engine_schematic(text_file)

    act_numbers = register_numbers(engine_schematic)
    assert act_numbers == [
        Number(value=467, line=0, position=(0, 2)),
        Number(value=114, line=0, position=(5, 7)),
        Number(value=35, line=2, position=(2, 3)),
        Number(value=633, line=2, position=(6, 8)),
        Number(value=617, line=4, position=(0, 2)),
        Number(value=58, line=5, position=(7, 8)),
        Number(value=592, line=6, position=(2, 4)),
        Number(value=755, line=7, position=(6, 8)),
        Number(value=664, line=9, position=(1, 3)),
        Number(value=598, line=9, position=(5, 7)),
    ]

    assert [number.symbols(engine_schematic) for number in act_numbers] == [
        set("*"),
        set(),
        set("*"),
        set("#"),
        set("*"),
        set(),
        set("+"),
        set("*"),
        set("$"),
        set("*"),
    ]

    assert [number.is_part_number(engine_schematic) for number in act_numbers] == [
        True,
        False,
        True,
        True,
        True,
        False,
        True,
        True,
        True,
        True,
    ]


def test_find_part_numbers(text_file):
    engine_schematic = get_engine_schematic(text_file)

    act_part_nums = find_part_numbers(engine_schematic)

    assert act_part_nums == [
        Number(value=467, line=0, position=(0, 2)),
        Number(value=35, line=2, position=(2, 3)),
        Number(value=633, line=2, position=(6, 8)),
        Number(value=617, line=4, position=(0, 2)),
        Number(value=592, line=6, position=(2, 4)),
        Number(value=755, line=7, position=(6, 8)),
        Number(value=664, line=9, position=(1, 3)),
        Number(value=598, line=9, position=(5, 7)),
    ]

    assert sum([num.value for num in act_part_nums]) == 4361
