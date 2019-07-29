from .line_counter import LineCounter
from .matcher import Matcher
from .directory_tree import DirectoryTree, Node


def line_counter():
    return LineCounter()


def matcher():
    return Matcher()


def directory_tree():
    return DirectoryTree


def node():
    return Node
