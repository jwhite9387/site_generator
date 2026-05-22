from textnode import *
from htmlnode import *
from markdown_to_blocks import *
from text_to_textnodes import *


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            block_nodes.append(paragraph_block(block))
        elif block_type == BlockType.HEADING:
            block_nodes.append(heading_block(block))
        elif block_type == BlockType.QUOTE:
            block_nodes.append(quote_block(block))
        elif block_type == BlockType.ULIST:
            block_nodes.append(ulist_block(block))
        elif block_type == BlockType.OLIST:
            block_nodes.append(olist_block(block))
        elif block_type == BlockType.CODE:
            block_nodes.append(code_block(block))
    parent_node = ParentNode("div", block_nodes)
    return parent_node
        

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    htmlnodes = []
    for node in textnodes:
        htmlnodes.append(text_node_to_html_node(node))
    return htmlnodes

def paragraph_block(block):
    new_block = block.replace("\n", " ")
    children = text_to_children(new_block)
    return ParentNode("p", children)

def heading_block(block):
    count = 0
    for character in block:
        if character == "#":
            count += 1
        else:
            break
    if count > 6:
        raise Exception("Invalid heading level: Must be 1-6")
    tag_name = "h" + str(count)
    new_block = block[count + 1:]
    children = text_to_children(new_block)
    return ParentNode(tag_name, children)

def quote_block(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.removeprefix(">").lstrip())
    new_string = " ".join(new_lines)
    children = text_to_children(new_string)
    return ParentNode("blockquote", children)

def ulist_block(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_line = line.removeprefix("- ")
        child = text_to_children(new_line)
        child_node = ParentNode("li", child)
        new_lines.append(child_node)
    return ParentNode("ul", new_lines)

def olist_block(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_line = line.split(". ", 1)
        child = text_to_children(new_line[1])
        child_node = ParentNode("li", child)
        new_lines.append(child_node)
    return ParentNode("ol", new_lines)

def code_block(block):
    first_newline = block.find("\n")
    new_block = block[first_newline + 1:-3]
    code_node = TextNode(new_block, TextType.TEXT)
    html = text_node_to_html_node(code_node)
    code_parent = ParentNode("code", [html])
    return ParentNode("pre", [code_parent])