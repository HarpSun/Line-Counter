import os

from directory_tree import DirectoryTree, Node


class LineCounter:
    # TODO commandline func
    # TODO ignore file func

    def __init__(self) -> None:
        self._extension_list = []
        self._exclude_list = []
        self._total_lines = 0

    def lines_from_path(
            self, path: str, *, exclude: list = None, extension: list = None
    ) -> int:
        """
            exclude contains list of file or dir not to be counted
            extension contains list of ext intend to be counted
            when passed together exclude will work first
        """
        if exclude:
            self._exclude_list.extend(exclude)
        if extension:
            self._extension_list.extend(extension)
        dir_tree = DirectoryTree(path)
        file_list = dir_tree.traversal_with_filter(self._exclude_list, self._extension_list)
        for n in file_list:
            self._total_lines += self.lines_from_file(n)
        return self._total_lines

    @staticmethod
    def lines_from_file(node: Node) -> int:
        with open(node.path, 'r', errors='ignore') as f:
            lines = f.readlines()
            return len(lines)


if __name__ == '__main__':
    counter = LineCounter()
    total = counter.lines_from_path(
        '../../hua_crm',
        extension=['py']
    )
    print(total)
