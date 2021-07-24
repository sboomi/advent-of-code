from src import day_3


def test_d3_p1():
    test_forest = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]
    actual = day_3.d3_p1(test_forest)
    expected = 7
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_d3_p2():
    test_forest = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]
    actual = day_3.d3_p2(test_forest)
    expected = 336
    assert actual == expected, f"Expected {expected}, got {actual}"
