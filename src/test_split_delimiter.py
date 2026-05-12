import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextType, TextNode


class TestSplitDelimiter(unittest.TestCase):

    def test_code_delimiter(self):
        node = TextNode("This has a `code phrase` inside", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This has a ", TextType.TEXT),
                TextNode("code phrase", TextType.CODE),
                TextNode(" inside", TextType.TEXT),
            ],
        )

    def test_bold_delimiter(self):
        node = TextNode("This has a **bold phrase** inside", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This has a ", TextType.TEXT),
                TextNode("bold phrase", TextType.BOLD),
                TextNode(" inside", TextType.TEXT),
            ],
        )

    def test_italic_delimiter(self):
        node = TextNode("This has an _italic phrase_ inside", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This has an ", TextType.TEXT),
                TextNode("italic phrase", TextType.ITALIC),
                TextNode(" inside", TextType.TEXT),
            ],
        )

    def test_unclosed_delimiter(self):
        node = TextNode("This has an **unclosed bold phrase", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_non_text_delimiter(self):
        node1 = TextNode("This is a **non-text** type node", TextType.BOLD)
        node2 = TextNode("This is a **bold text** node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a **non-text** type node", TextType.BOLD),
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" node", TextType.TEXT),
            ],
        )