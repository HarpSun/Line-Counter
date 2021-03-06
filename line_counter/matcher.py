import typing


class Matcher:
    """
        Matcher, act as a filter of files and directory that should
        not be counted
     """

    def __init__(
            self, *,
            exclude_files: typing.Iterable[str] = None,
            exclude_dirs: typing.Iterable[str] = None,
            exclude_extensions: typing.Iterable[str] = None,
            accept_extensions: typing.Iterable[str] = None,
    ) -> None:
        # same extension cannot be assigned to exclude and accept at the same time
        self._check_extension_conflict(exclude_extensions, accept_extensions)
        self._exclude_files = set(exclude_files) if exclude_files else set()
        self._exclude_dirs = set(exclude_dirs) if exclude_dirs else set()
        self._exclude_extensions = set(exclude_extensions) if exclude_extensions else set()
        self._accept_extensions = set(accept_extensions) if accept_extensions else set()

    @classmethod
    def init_by_file(cls, path: str) -> 'Matcher':
        exclude_files = set()
        exclude_dirs = set()
        exclude_extensions = set()
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith('#') or len(line) == 0:
                    continue
                if line.startswith('*.'):
                    ext = line.split('.')[-1]
                    exclude_extensions.add(ext)
                elif line.endswith('/'):
                    name = line[:-1]
                    exclude_dirs.add(name)
                else:
                    exclude_files.add(line)
            return cls(
                exclude_files=exclude_files,
                exclude_dirs=exclude_dirs,
                exclude_extensions=exclude_extensions
            )

    def match_file_by_name(self, name: str) -> bool:
        """return False means file should be counted"""
        if '.' in name:
            ext = name.split('.')[-1]
        else:
            ext = ''
        # match exclude
        if self._exclude_files and name in self._exclude_files:
            return True
        if self._exclude_extensions and ext in self._exclude_extensions:
            return True
        if self._accept_extensions:
            return ext not in self._accept_extensions
        return False

    def match_dir_by_name(self, name: str) -> bool:
        if self._exclude_dirs:
            return name in self._exclude_dirs
        else:
            return False

    def _check_extension_conflict(self, exclude_extensions, accept_extensions):
        if exclude_extensions and accept_extensions:
            if exclude_extensions & accept_extensions:
                raise ValueError('extension conflict')
