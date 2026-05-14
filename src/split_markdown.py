from textnode import TextNode, TextType
from extract_markdown import extract_markdown_links, extract_markdown_images


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        image_node = extract_markdown_images(old_node.text)
        if len(image_node) == 0:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for tup in image_node:
            sections = original_text.split(f"![{tup[0]}]({tup[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(tup[0], TextType.IMAGE, tup[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        link_node = extract_markdown_links(old_node.text)
        if len(link_node) == 0:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for tup in link_node:
            sections = original_text.split(f"[{tup[0]}]({tup[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(tup[0], TextType.LINK, tup[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes