from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    text_node = TextNode("some text", TextType.LINK, "https://example.com")
    print(text_node)
    html_node = HTMLNode("a", "paragraph text", [], {"href": "https://google.com", "target": "_blank"})
    print(html_node)
    


main()