import pytest
from ac2022python.solutions.day7 import (
    TreeNode,
    Folder,
    File,
    FileSystem,
    NoSpaceLeftOnDevice,
)

EXAMPLE_INPUT = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    txt = "\n".join(EXAMPLE_INPUT)
    fn = tmp_path_factory.mktemp("data") / "day7"
    with open(fn, "w") as f:
        f.write(txt)
    return fn


@pytest.fixture
def obj_fs() -> FileSystem:
    fs = FileSystem()

    children_nodes: list[TreeNode] = [
        Folder("a"),
        File("b.txt", 14848514),
        File("c.dat", 8504156),
        Folder("d"),
    ]

    for child in children_nodes:
        fs.append_to_current_dir(child)

    fs.current_dir = fs.dirs["/a"]

    children_nodes = [
        Folder("e"),
        File("f", 29116),
        File("g", 2557),
        File("h.lst", 62596),
    ]

    for child in children_nodes:
        fs.append_to_current_dir(child)

    fs.current_dir = fs.dirs["/a/e"]
    fs.append_to_current_dir(File("i", 584))

    fs.current_dir = fs.dirs["/d"]

    children_nodes = [
        File("j", 4060174),
        File("d.log", 8033020),
        File("d.ext", 5626152),
        File("k", 7214296),
    ]

    for child in children_nodes:
        fs.append_to_current_dir(child)

    return fs


def test_root_node():
    root_node = Folder("/")

    assert str(root_node) == "/"
    assert len(root_node.parents) == 0
    assert root_node.children == {}


def test_append_children_root_node():
    root_node: Folder = Folder("/")
    children_nodes: list[TreeNode] = [
        Folder("a"),
        File("b.txt", 14848514),
        File("c.dat", 8504156),
        Folder("d"),
    ]
    expected_names = ["/a", "/b.txt", "/c.dat", "/d"]

    for child, name in zip(children_nodes, expected_names):
        child.parents.append(root_node)
        root_node.children[child.name] = child
        assert len(child.parents) == 1
        assert str(child) == name

    assert len(root_node.children.keys()) == 4


def test_append_to_dirs_construct_tree():
    fs = FileSystem()
    assert fs.current_dir.name == "/"
    assert len(fs.dirs) == 1

    children_nodes: list[TreeNode] = [
        Folder("a"),
        File("b.txt", 14848514),
        File("c.dat", 8504156),
        Folder("d"),
    ]

    expected_names = ["/a", "/b.txt", "/c.dat", "/d"]

    for child, exp_name in zip(children_nodes, expected_names):
        node_name = child.name
        fs.append_to_current_dir(child)
        assert fs.dirs.get(exp_name) is not None
        assert str(fs.dirs[exp_name]) == exp_name
        assert fs.dirs[exp_name].name == node_name
        assert len(fs.dirs[exp_name].parents) == 1
        assert str(fs.dirs[exp_name]) == str(child)
        assert fs.dirs[exp_name].name == child.name
        assert len(fs.dirs[exp_name].parents) == len(child.parents)

    assert len(fs.current_dir.children) == 4
    assert len(fs.dirs) == 5

    # next iter
    fs.current_dir = fs.dirs["/a"]
    assert fs.current_dir.name == "a"
    assert len(fs.current_dir.parents) == 1
    assert len(fs.current_dir.children) == 0

    children_nodes = [
        Folder("e"),
        File("f", 29116),
        File("g", 2557),
        File("h.lst", 62596),
    ]

    expected_names = ["/a/e", "/a/f", "/a/g", "/a/h.lst"]

    for child, exp_name in zip(children_nodes, expected_names):
        node_name = child.name
        fs.append_to_current_dir(child)
        assert fs.dirs.get(exp_name) is not None
        assert str(fs.dirs[exp_name]) == exp_name
        assert fs.dirs[exp_name].name == node_name
        assert len(fs.dirs[exp_name].parents) == 2
        assert str(fs.dirs[exp_name]) == str(child)
        assert fs.dirs[exp_name].name == child.name
        assert len(fs.dirs[exp_name].parents) == len(child.parents)

    assert len(fs.current_dir.children) == 4
    assert len(fs.dirs) == 9

    # Next iter
    fs.current_dir = fs.dirs["/a/e"]
    assert fs.current_dir.name == "e"
    assert len(fs.current_dir.parents) == 2
    assert len(fs.current_dir.children) == 0

    fs.append_to_current_dir(File("i", 584))
    assert fs.dirs.get("/a/e/i") is not None
    assert str(fs.dirs["/a/e/i"].name) == "i"
    assert len(fs.dirs["/a/e/i"].parents) == 3
    assert len(fs.current_dir.children) == 1
    assert len(fs.dirs) == 10

    fs.current_dir = fs.dirs["/d"]
    assert fs.current_dir.name == "d"
    assert len(fs.current_dir.parents) == 1
    assert len(fs.current_dir.children) == 0

    children_nodes = [
        File("j", 4060174),
        File("d.log", 8033020),
        File("d.ext", 5626152),
        File("k", 7214296),
    ]

    expected_names = ["/d/j", "/d/d.log", "/d/d.ext", "/d/k"]

    for child, exp_name in zip(children_nodes, expected_names):
        node_name = child.name
        fs.append_to_current_dir(child)
        assert fs.dirs.get(exp_name) is not None
        assert str(fs.dirs[exp_name]) == exp_name
        assert fs.dirs[exp_name].name == node_name
        assert len(fs.dirs[exp_name].parents) == 2
        assert str(fs.dirs[exp_name]) == str(child)
        assert fs.dirs[exp_name].name == child.name
        assert len(fs.dirs[exp_name].parents) == len(child.parents)

    assert len(fs.current_dir.children) == 4
    assert len(fs.dirs) == 14


def test_move_to_directory(obj_fs: FileSystem):
    obj_fs.cd("/")

    assert obj_fs.current_dir.name == "/"
    assert len(obj_fs.current_dir.children) == 4

    obj_fs.cd("a")
    assert obj_fs.current_dir.name == "a"
    assert str(obj_fs.current_dir) == "/a"
    assert len(obj_fs.current_dir.children) == 4

    obj_fs.cd("e")
    assert obj_fs.current_dir.name == "e"
    assert len(obj_fs.current_dir.parents) == 2
    assert str(obj_fs.current_dir) == "/a/e"
    assert len(obj_fs.current_dir.children) == 1

    # .. go back to 'a'
    obj_fs.cd("..")
    assert obj_fs.current_dir.name == "a"
    assert str(obj_fs.current_dir) == "/a"
    assert len(obj_fs.current_dir.children) == 4

    # ..go back to root
    obj_fs.cd("..")
    assert obj_fs.current_dir.name == "/"
    assert len(obj_fs.current_dir.children) == 4

    # head to d
    obj_fs.cd("d")
    assert obj_fs.current_dir.name == "d"
    assert str(obj_fs.current_dir) == "/d"
    assert len(obj_fs.current_dir.children) == 4


def test_folder_total_size(obj_fs: FileSystem):
    obj_fs.current_dir = obj_fs.dirs["/a/e"]

    actual_ts = obj_fs.current_dir.total_size()
    expected_ts = 584

    assert expected_ts == actual_ts

    obj_fs.current_dir = obj_fs.dirs["/a"]
    actual_ts = obj_fs.current_dir.total_size()
    expected_ts = 94853
    assert expected_ts == actual_ts

    obj_fs.current_dir = obj_fs.dirs["/d"]
    actual_ts = obj_fs.current_dir.total_size()
    expected_ts = 24933642
    assert expected_ts == actual_ts

    obj_fs.current_dir = obj_fs.dirs["/"]
    actual_ts = obj_fs.current_dir.total_size()
    expected_ts = 48381165
    assert expected_ts == actual_ts


def test_no_space_left_part_one(text_file):
    nslod = NoSpaceLeftOnDevice()

    act_result = nslod.find_sum_smallest_subdirs(text_file)
    exp_result = 95437

    act_result == exp_result


def test_no_space_left_part_two(text_file):
    nslod = NoSpaceLeftOnDevice()

    act_result = nslod.find_smallest_dir_size_to_delete(text_file)
    exp_result = 24933642

    act_result == exp_result
