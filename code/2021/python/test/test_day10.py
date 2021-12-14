import pytest
from src.day10 import check_legal_chunks


def test_check_legal_chunks_valid_chunks():
    list_valid_chunks = ["([])", "{()()()}", "<([{}])>", "[<>({}){}[([])<>]]", "(((((((((())))))))))"]
    exp_are_valid = ["valid" for _ in list_valid_chunks]
    act_are_valid = [check_legal_chunks(chunk)[0] for chunk in list_valid_chunks]

    assert exp_are_valid == act_are_valid, f"Expected\n{exp_are_valid}\nGot\n{act_are_valid}"


def test_check_legal_chunks_corrupted_chunks():
    list_corrupted_chunks = ["(]", "{()()()>", "(((()))}", "<([]){()}[{}])]"]
    exp_are_valid = ["corrupted" for _ in list_corrupted_chunks]
    act_are_valid = [check_legal_chunks(chunk)[0] for chunk in list_corrupted_chunks]

    assert exp_are_valid == act_are_valid, f"Expected\n{exp_are_valid}\nGot\n{act_are_valid}"


def test_check_legal_chunks_bigger_example():
    test_nav_sys = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]

    exp_line_status = [
        "incomplete",
        "incomplete",
        "corrupted",
        "incomplete",
        "corrupted",
        "corrupted",
        "incomplete",
        "corrupted",
        "corrupted",
        "incomplete",
    ]

    act_line_status = [check_legal_chunks(chunk)[0] for chunk in test_nav_sys]
    assert exp_line_status == act_line_status, f"Expected\n{exp_line_status}\nGot\n{act_line_status}"
