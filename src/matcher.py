class Matcher:
    """
        exclude contains list of file or dir not to be counted
        extension contains list of ext intend to be counted
        when passed together exclude will work first
     """

    def __init__(self, *, exclude: list = None, extension: list = None) -> None:
        self._exclude_list = list(exclude) if exclude else []
        self._extension_list = list(extension) if extension else []

    def match_name(self, pattern: str) -> bool:
        if self._exclude_list:
            return pattern not in self._exclude_list
        else:
            return True

    def match_extension(self, pattern: str) -> bool:
        if self._extension_list:
            return pattern in self._extension_list
        else:
            return True
