class Matcher:
    """
        exclude contains list of file or dir not to be counted
        extension contains list of ext intend to be counted
        when passed together exclude will work first
     """

    def __init__(
            self, *,
            exclude_files: list = None,
            exclude_dirs: list = None,
            exclude_extensions: list = None,
    ) -> None:
        self._exclude_files = list(exclude_files) if exclude_files else []
        self._exclude_dirs = list(exclude_dirs) if exclude_dirs else []
        self._exclude_extensions = list(exclude_extensions) if exclude_extensions else []

    @classmethod
    def init_by_file(cls, path: str) -> None:
        exclude_files = []
        exclude_dirs = []
        exclude_extensions = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith('#'):
                    continue
                if line.startswith('*.'):
                    ext = line.split('.')[-1]
                    exclude_extensions.append(ext)
                elif line.endswith('/'):
                    name = line[:-1]
                    exclude_dirs.append(name)
                # TODO deal with anti ignore logic
                elif line.startswith('!'):
                    pass
                else:
                    exclude_files.append(line)
            cls(
                exclude_files=exclude_files,
                exclude_dirs=exclude_dirs,
                exclude_extensions=exclude_extensions
            )

    def match_file_by_name(self, name: str) -> bool:
        if '.' in name:
            ext = name.split('.')
        else:
            ext = ''
        # match exclude
        if self._exclude_files and name in self._exclude_files:
            return True
        if self._exclude_extensions and ext in self._exclude_extensions:
            return True

    def match_dir_by_name(self, name: str) -> bool:
        return self._exclude_dirs and name in self._exclude_dirs
