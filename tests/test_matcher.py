from unittest import TestCase, main

from line_counter import Matcher


class TestMatcher(TestCase):
    file = 'data/ignore.txt'
    matcher = Matcher.init_by_file(file)

    def test_init_by_file(self):
        self.assertEqual(['ignoreA'], self.matcher._exclude_dirs)
        self.assertEqual(['ignore.py'], self.matcher._exclude_files)
        self.assertEqual(['py'], self.matcher._exclude_extensions)

    def test_match_dir_by_name(self):
        self.assertEqual(True, self.matcher.match_dir_by_name('ignoreA'))

    def test_match_file_by_name(self):
        self.assertEqual(True, self.matcher.match_file_by_name('ignore.py'))
        self.assertEqual(True, self.matcher.match_file_by_name('test.py'))


if __name__ == '__main__':
    main()
