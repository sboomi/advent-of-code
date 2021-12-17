import pytest
from src.day10 import (
    check_legal_chunks,
    get_first_wrong_closing_chr,
    syntax_score,
    make_mirror_image,
    get_completion_score,
    middle_score,
)


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


def test_get_first_wrong_closing_chr():
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

    exp_wrong_chrs = "})])>"
    act_wrong_chrs = "".join([get_first_wrong_closing_chr(line) for line in test_nav_sys])

    assert exp_wrong_chrs == act_wrong_chrs, f"Expected {exp_wrong_chrs}. Got {act_wrong_chrs}."


def test_syntax_score():
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

    act_syntax_score = syntax_score(test_nav_sys)
    exp_syntax_score = 26397

    assert act_syntax_score == exp_syntax_score, f"Expected {exp_syntax_score}. Got {act_syntax_score}."


def test_make_mirror_image():
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

    exp_mirror_images = [
        "}}]])})]",
        ")}>]})",
        "",
        "}}>}>))))",
        "",
        "",
        "]]}}]}]}>",
        "",
        "",
        "])}>",
    ]

    act_mirror_images = [make_mirror_image(line) for line in test_nav_sys]
    assert exp_mirror_images == act_mirror_images, f"Expected\n{exp_mirror_images}\nGot\n{act_mirror_images}"


def test_get_completion_score():
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

    exp_score_list = [
        288957,
        5566,
        -1,
        1480781,
        -1,
        -1,
        995444,
        -1,
        -1,
        294,
    ]

    act_score_list = [get_completion_score(line) for line in test_nav_sys]
    assert exp_score_list == act_score_list, f"Expected\n{exp_score_list}\nGot\n{act_score_list}"


def test_middle_score():
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

    act_middle_score = middle_score(test_nav_sys)
    exp_middle_score = 288957

    assert act_middle_score == exp_middle_score, f"Expected {exp_middle_score}. Got {act_middle_score}."
