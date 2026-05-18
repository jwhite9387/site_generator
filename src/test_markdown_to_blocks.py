import unittest

from markdown_to_blocks import *


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded paragraph**

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded paragraph**",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items"
            ],
        )

    def test_markdown_to_blocks_empty(self):
        md = """
This is a normal paragraph


    This paragraph has leading whitespace

        
This paragraph has trailing whitespace    


Empty block above
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a normal paragraph",
                "This paragraph has leading whitespace",
                "This paragraph has trailing whitespace",
                "Empty block above"
            ],
        )

    def test_block_to_block_heading(self):
        block1 = "# This is a heading"
        block2 = "## This is a heading"
        block3 = "###This is a paragraph"
        blocks = [block1, block2, block3]
        block_types = []
        for block in blocks:
            block_types.append(block_to_block_type(block))

        self.assertListEqual([BlockType.HEADING, BlockType.HEADING, BlockType.PARAGRAPH], block_types)

    def test_block_to_block_code(self):
        block = """```
        This is a block of code
        ```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_quote(self):
        block1 = ">This is a block of quote"
        block2 = "> This is a block of quote"
        block3 = """>
        This is a block of quote
        """
        
        blocks = [block1, block2, block3]
        block_types = []
        for block in blocks:
            block_types.append(block_to_block_type(block))

        self.assertListEqual([BlockType.QUOTE, BlockType.QUOTE, BlockType.PARAGRAPH], block_types)

    def test_block_to_block_ulist(self):
        block = "- first item" \
        "- second item" \
        "- third item"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)

    def test_block_to_block_olist(self):
        block = "1. first item" \
        "2. second item" \
        "3. third item"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)