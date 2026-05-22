import unittest

from markdown_to_html import *
from htmlnode import *


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md1 = """
# This is an **h1** heading
"""
        md2 = """
## This is an _h2_ heading

"""

        nodes = [markdown_to_html_node(md1), markdown_to_html_node(md2)]
        html_nodes = []
        for node in nodes:
            html = node.to_html()
            html_nodes.append(html)
        self.assertListEqual(
            html_nodes,
            [
                "<div><h1>This is an <b>h1</b> heading</h1></div>",
                "<div><h2>This is an <i>h2</i> heading</h2></div>"
            ],
        )

    def test_quotes(self):
        md = """
> This is a quote
> block of text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><blockquote>This is a quote block of text</blockquote></div>",
        )

    def test_ulist(self):
        md = """
- This is an
- **unordered** list of
- _items_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an</li><li><b>unordered</b> list of</li><li><i>items</i></li></ul></div>",
        )

    def test_olist(self):
        md = """
1. This is an
2. _ordered_ list of
3. **items**
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an</li><li><i>ordered</i> list of</li><li><b>items</b></li></ol></div>",
        )