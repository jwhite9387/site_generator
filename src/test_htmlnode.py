import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType


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

    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_parent_to_html_multiple_children(self):
        first_child = LeafNode("b", "first child")
        second_child = LeafNode("i", "second child")
        third_child = LeafNode("a", "third child", {"href": "https://google.com"})
        parent_node = ParentNode("span", [first_child, second_child, third_child], {"href": "https://boot.dev"})
        self.assertEqual(parent_node.to_html(), 
                         '<span href="https://boot.dev"><b>first child</b><i>second child</i><a href="https://google.com">third child</a></span>')
    
    def test_parent_to_html_no_children(self):
        parent_node = ParentNode("span", [])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_text(self):
        node = TextNode("plain text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "plain text node")

    def test_bold(self):
        node = TextNode("bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>bold text node</b>")
    
    def test_italic(self):
        node = TextNode("italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>italic text node</i>")

    def test_code(self):
        node = TextNode("code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>code text node</code>")

    def test_link(self):
        node = TextNode("link text node", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://example.com">link text node</a>')

    def test_image(self):
        node = TextNode("image text node", TextType.IMAGE, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="https://example.com" alt="image text node"></img>')

    def test_invalid(self):
        node = TextNode("invalid text node", "invalid")
        with self.assertRaises(Exception):
            html_node = text_node_to_html_node(node)
            html_node.to_html()