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
        self.assertNotEqual(node.to_html(), "<P>Hello, world!</P>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me!", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">Click Me!</a>')
        self.assertNotEqual(node.to_html(), '<a href="https://google.com">Click Me?</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "This is bold text.")
        self.assertEqual(node.to_html(), "<b>This is bold text.</b>")
        self.assertNotEqual(node.to_html(), "<b>This is italic text.</b>")