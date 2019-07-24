import argparse
import typing
import time

from .directory_tree import DirectoryTree, Node


class LineCounter:

    def __init__(self) -> None:
        self._extension_list = []
        self._exclude_list = []
        self.total_files = 0
        self.total_lines = 0

    def lines_from_path(
            self, path: str,
            *,
            exclude: typing.List[str] = None,
            extension: typing.List[str] = None
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
        # while iterating dir_tree, directory excluded should not be yield
        dir_tree._exclude_list = self._exclude_list
        for file in dir_tree:
            if file.name in self._exclude_list:
                continue
            if self._extension_list:
                ext = file.name.split('.')[-1]
                if ext in self._extension_list:
                    self.total_files += 1
                    self.total_lines += self.lines_from_file(file)
            else:
                self.total_files += 1
                self.total_lines += self.lines_from_file(file)
        return self.total_lines

    def lines_from_file(self, node: Node) -> int:
        with open(node.path, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(bl.count('\n') for bl in self._blocks(f))

    @staticmethod
    def _blocks(
            file: typing.IO,
            size: int = 65536
    ) -> typing.Generator[str, None, None]:
        while True:
            b = file.read(size)
            if not b:
                break
            yield b


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='lc',
        description='total lines of a file or dir'
    )
    parser.add_argument(
        'path', metavar='path', type=str, help='path of target'
    )
    parser.add_argument(
        '--exclude', action='store', type=str, nargs='*', help='file or dir to be ignored'
    )
    parser.add_argument(
        '--ext', action='store', type=str, nargs='*', help='extension of file to be counted'
    )
    args = parser.parse_args()
    path = args.path
    if path.endswith('/'):
        path = path[:-1]
    exclude_list = []
    extension_list = []
    if args.exclude:
        exclude_list = args.exclude
    if args.ext:
        extension_list = args.ext
    # execute
    counter = LineCounter()
    start = time.time()
    total = counter.lines_from_path(
        path,
        exclude=exclude_list,
        extension=extension_list
    )
    end = time.time()
    print('total lines:', total)
    print('{} files searched'.format(counter.total_files))
    print('takes {:2f} seconds'.format(end-start))


if __name__ == '__main__':
    main()
