import os
import typing
from sys import platform


if platform == "darwin":
    SPLIT_SIGN = '/'
elif platform == "win32":
    SPLIT_SIGN = '\\'
else:
    raise SystemError('unknown operating system')


class Node:

    def __init__(self, path: str) -> None:
        self.path = path
        self.name = path.split(SPLIT_SIGN)[-1]
        self.type = _type_by_path(path)
        self.children = []

    def __repr__(self) -> str:
        s = ''
        for attr, value in self.__dict__.items():
            s += '{}: ({})\n'.format(attr, value)
        return '< \n{} >\n'.format(s)


class DirectoryTree:

    def __init__(self, path: str) -> None:
        self.root = Node(path)
        self._generate_tree_from_root(self.root)

    def __iter__(self) -> typing.Generator:
        root = self.root
        if not root.children:
            if root.type == 'file':
                yield self.root
            elif root.type == 'directory':
                yield
        # breadth first traversal
        queue = [root]
        while queue:
            node = queue.pop(0)
            for child in node.children:
                if child.type == 'file':
                    yield child
                elif child.type == 'directory':
                    queue.append(child)

    def _generate_tree_from_root(self, root: Node) -> None:
        if root.type == 'directory':
            subdir_list = os.listdir(root.path)
            for sub in subdir_list:
                path = os.path.join(root.path, sub)
                node = Node(path)
                root.children.append(node)
                self._generate_tree_from_root(node)


def _type_by_path(path: str) -> str:
    if os.path.isfile(path):
        return 'file'
    elif os.path.isdir(path):
        return 'directory'
    else:
        raise ValueError('{} is not a valid path'.format(path))
