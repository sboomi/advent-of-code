"""Day 7: No Space Left On Device"""
from pathlib import Path
from typing import Optional

from rich import print

from ac2022python.solutions import DATA_PATH

PUZZLE_INPUT = Path(DATA_PATH / "day7")


class TreeNode:
    """Base class for the file system, which has a name and can memorize its parents"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.parents: list[Folder] = []

    def __str__(self) -> str:
        return "/".join(
            [parent.name if parent.name != "/" else "" for parent in self.parents]
            + [self.name]
        )

    def is_file(self) -> bool:
        return isinstance(self, File)

    def is_folder(self) -> bool:
        return isinstance(self, Folder)


class Folder(TreeNode):
    """Folder structure that can append children to it for an easy access through `cd`."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.children: dict[str, TreeNode] = {}
        self.dir_size: int = 0

    def total_size(self) -> int:
        """Returns the total size from the directory.

        Subdirectories are also included through recursion.

        Returns
        -------
        int
            The total size in bytes from the directory.
        """
        ts = 0
        for child in self.children.values():
            if child.is_file():
                ts += child.size
            else:
                ts += child.total_size()
        self.dir_size = ts
        return ts


class File(TreeNode):
    """The File structure is at the bottom of the tree navigation.
    It has a size in bytes.
    """

    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self.size = size


class FileSystem:
    """The FileSystem is the manager of the files and folders from the problem.
    It starts with the root folder and keeps a memo as the `dirs` attribute for
    an easy access. The `current_dir` is necessary for appending operations and
    quick access.
    """

    def __init__(self) -> None:
        self.dirs: dict[str, TreeNode] = {"/": Folder("/")}
        self.current_dir: Folder = self.dirs["/"]

    def walk(self) -> list[str]:
        """Returns a list of the folders, files
        and subfolders of the file system

        Returns
        -------
        list[str]
            A list of folders and subfolders
        """
        return list(self.dirs.keys())

    def dir_sizes(
        self, min_bytes: Optional[int] = None, max_bytes: Optional[int] = None
    ) -> list[tuple[str, int]]:
        """_summary_

        Parameters
        ----------
        min_bytes : Optional[int], optional
            _description_, by default None
        max_bytes : Optional[int], optional
            _description_, by default None

        Returns
        -------
        list[tuple[str, int]]
            _description_
        """

        ds = []
        for node in self.dirs.values():
            if node.is_folder():
                if (
                    (
                        min_bytes is not None
                        and max_bytes is not None
                        and min_bytes <= node.dir_size <= max_bytes
                    )
                    or (
                        min_bytes is None
                        and max_bytes is not None
                        and node.dir_size <= max_bytes
                    )
                    or (
                        min_bytes is not None
                        and max_bytes is None
                        and min_bytes <= node.dir_size
                    )
                    or (min_bytes is None and max_bytes is None)
                ):
                    ds.append((str(node), node.dir_size))
        return ds

    def cd(self, dir_name: str) -> Folder:
        """_summary_

        Parameters
        ----------
        dir_name : str
            _description_

        Returns
        -------
        Folder
            _description_
        """
        if dir_name == "/":
            self.current_dir = self.dirs["/"]
            return self.current_dir

        if dir_name == "..":
            self.current_dir = self.current_dir.parents[-1]
            return self.current_dir

        if self.current_dir.children.get(dir_name):
            self.current_dir = self.current_dir.children.get(dir_name)
            return self.current_dir

        return self.current_dir

    def append_to_current_dir(self, child_node: TreeNode):
        """_summary_

        Parameters
        ----------
        child_node : TreeNode
            _description_
        """
        child_node.parents.extend(self.current_dir.parents)
        child_node.parents.append(self.current_dir)
        self.current_dir.children[child_node.name] = child_node
        if child_node.is_file():
            self.current_dir.dir_size += child_node.size
        self.dirs[str(child_node)] = child_node


class NoSpaceLeftOnDevice:
    def __init__(self) -> None:
        self.fs = FileSystem()
        self.append_mode = False

    def evaluate_fs_size(self):
        """Takes the file structure and computes the total size for each directory"""
        self.fs.cd("/")
        self.fs.current_dir.total_size()

    def create_tree(self, log_output: Path):
        """Takes a file output; reads the instructions and builds the file structure

        Parameters
        ----------
        log_output : Path
            _description_
        """
        with open(log_output, "r") as f_out:
            for line_out in f_out:
                if self.append_mode and not line_out.startswith("$ cd"):
                    if line_out.startswith("dir"):
                        child_node = Folder(line_out.split()[1].strip())
                    elif line_out[0].isdigit():
                        child_node = File(
                            line_out.split()[1].strip(),
                            int(line_out.split()[0].strip()),
                        )
                    self.fs.append_to_current_dir(child_node)

                if line_out.startswith("$ cd"):
                    self.append_mode = False

                    _, _, dir_name = [w.strip() for w in line_out.split()]
                    self.fs.cd(dir_name)

                if line_out.startswith("$ ls"):
                    self.append_mode = True

    def find_sum_smallest_subdirs(self, log_output: Path) -> int:
        n_bytes = 0

        self.create_tree(log_output)
        self.evaluate_fs_size()

        for _, size in self.fs.dir_sizes(max_bytes=100000):
            n_bytes += size

        return n_bytes

    def find_smallest_dir_size_to_delete(self, log_output: Path) -> int:
        self.create_tree(log_output)
        self.evaluate_fs_size()
        space_to_free = 30000000 - (70000000 - self.fs.dirs["/"].dir_size)

        return sorted(
            self.fs.dir_sizes(min_bytes=space_to_free), key=lambda dsize: dsize[1]
        )[0][1]


def solve_first_part():
    nslod = NoSpaceLeftOnDevice()
    res = nslod.find_sum_smallest_subdirs(PUZZLE_INPUT)
    print(
        f"The sum of the total size of the subdirectories under 100k bytes is {res} bytes"
    )


def solve_second_part():
    nslod = NoSpaceLeftOnDevice()
    res = nslod.find_smallest_dir_size_to_delete(PUZZLE_INPUT)
    print(f"The sum regained from subdir deletion is {res}")


def solve_all():
    solve_first_part()
    solve_second_part()


if __name__ == "__main__":
    solve_all()
