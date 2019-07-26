from unittest import TestCase, main

from line_counter import LineCounter, Matcher


class LineCounterTest(TestCase):

    def test_lines_from_path(self):
        matcher = Matcher.init_by_file('data/ignore.txt')
        lc = LineCounter()
        total = lc.lines_from_path('data/testdir', matcher=matcher)
        self.assertEqual(3, total)


if __name__ == '__main__':
    main()
