import unittest

from split_markdown import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestSplitMarkdown(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [google](https://google.com) and another link [youtube](https://youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("google", TextType.LINK, "https://google.com"),
                TextNode(" and another link ", TextType.TEXT),
                TextNode("youtube", TextType.LINK, "https://youtube.com"),
            ],
            new_nodes,
        )

    def test_split_image_non_text(self):
        bold_node = TextNode(
            "This is a bold type textnode",
            TextType.BOLD,
        )
        italic_node = TextNode(
            "This is an italic type textnode",
            TextType.ITALIC,
        )
        image_node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([bold_node, italic_node, image_node])
        self.assertListEqual(
            [
                TextNode("This is a bold type textnode", TextType.BOLD),
                TextNode("This is an italic type textnode", TextType.ITALIC),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_link_non_text(self):
        bold_node = TextNode(
            "This is a bold type textnode",
            TextType.BOLD,
        )
        italic_node = TextNode(
            "This is an italic type textnode",
            TextType.ITALIC,
        )
        link_node = TextNode(
            "This is text with a link [google](https://google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([bold_node, italic_node, link_node])
        self.assertListEqual(
            [
                TextNode("This is a bold type textnode", TextType.BOLD),
                TextNode("This is an italic type textnode", TextType.ITALIC),
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("google", TextType.LINK, "https://google.com"),
            ],
            new_nodes,
        )

    def test_split_image_empty_string(self):
        empty_node = TextNode(
            "", 
            TextType.TEXT,
        )
        none_node = TextNode(
            None,
            TextType.TEXT,
        )
        image_node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([empty_node, none_node, image_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )