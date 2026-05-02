import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_eq(self):
        node = HTMLNode("p", "paragraph text", props={
            "href": "https://google.com", 
            "target": "_blank"
        })

        result = node.props_to_html()
        self.assertEqual(result, ' href="https://google.com" target="_blank"')

    def test_props_to_html_None(self):
        node = HTMLNode("p", "paragraph text")

        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "paragraph text")

        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")