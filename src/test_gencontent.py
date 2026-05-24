import unittest

from gencontent import *


class TestGencontent(unittest.TestCase):
    def test_extract_title(self):
        md1 = """
# Hello
"""
        title1 = extract_title(md1)
        self.assertEqual(
            title1,
            "Hello",
        )

        md2 = """
## No title here
"""
        with self.assertRaises(Exception):
            extract_title(md2)