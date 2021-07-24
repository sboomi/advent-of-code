from src import day_8


def test_d8_p1():
    test_instructions = [
        ("nop", 0),
        ("acc", 1),
        ("jmp", 4),
        ("acc", 3),
        ("jmp", -3),
        ("acc", -99),
        ("acc", 1),
        ("jmp", -4),
        ("acc", 6),
    ]
    actual = day_8.d8_p1(test_instructions)
    expected = 5
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_fix_kink():
    test_instructions = [
        ("nop", 0),
        ("acc", 1),
        ("jmp", 4),
        ("acc", 3),
        ("jmp", -3),
        ("acc", -99),
        ("acc", 1),
        ("jmp", -4),
        ("acc", 6),
    ]
    actual = day_8.fix_kink(test_instructions, -2)
    expected = [
        ("nop", 0),
        ("acc", 1),
        ("jmp", 4),
        ("acc", 3),
        ("jmp", -3),
        ("acc", -99),
        ("acc", 1),
        ("nop", -4),
        ("acc", 6),
    ]
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_d8_p2():
    test_instructions = [
        ("nop", 0),
        ("acc", 1),
        ("jmp", 4),
        ("acc", 3),
        ("jmp", -3),
        ("acc", -99),
        ("acc", 1),
        ("jmp", -4),
        ("acc", 6),
    ]
    actual = day_8.d8_p2(test_instructions)
    expected = 8
    assert actual == expected, f"Expected {expected}, got {actual}"
