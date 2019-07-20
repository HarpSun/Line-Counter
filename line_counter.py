import os


class LineCounter:

    def __init__(self):
        self._only_list = []
        self._exclude_list = []
        self._total_lines = 0

    def lines_from_path(self, path: str, *, exclude=None, only=None) -> int:
        """
            exclude and only can't be passed together, only one will work
        """
        if exclude and only:
            raise ValueError("exclude and only can't be passed together")
        if exclude:
            self._exclude_list = exclude
        if only:
            self._only_list = only

        target_name = path.split('/')[-1]
        if self._exclude_list:
            if target_name not in self._exclude_list:
                if os.path.isfile(path):
                    return self.lines_from_file(path)
                elif os.path.isdir(path):
                    return self.lines_from_directory(path)
            else:
                return 0

        if self._only_list:
            if os.path.isfile(path):
                if target_name in self._only_list:
                    return self.lines_from_file(path)
            elif os.path.isdir(path):
                return self.lines_from_directory(path)
            else:
                return 0

    def lines_from_directory(self, dir_path: str) -> int:
        self._total_lines = 0
        if not os.path.exists(dir_path):
            raise FileNotFoundError

        file_list = os.listdir(dir_path)
        for f in file_list:
            if f not in self._exclude_list:
                path = os.path.join(os.path.abspath(dir_path), f)
                if path.endswith('.py'):
                    self._total_lines += self.lines_from_file(path)
                elif os.path.isdir(path):
                    self._total_lines += self.lines_from_directory(path)

        return self._total_lines

    def lines_from_file(self, file_path: str) -> int:
        filename = file_path.split('/')[-1]
        if filename in self._exclude_list:
            return 0
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                return len(lines)

    def _filtered_file_list(self, path):
        result = []
        name = path.split('/')[-1]
        if os.path.isfile(path):
            if name in self._only_list:
                return result.append(path)
        elif os.path.isdir(path):
            return self.lines_from_directory(path)


if __name__ == '__main__':
    counter = LineCounter()
    total = counter.lines_from_path(
        '../test',
    )
    print(total)
