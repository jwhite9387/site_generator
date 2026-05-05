from textnode import TextType


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        
        raise NotImplementedError
    
    def props_to_html(self):
        if (self.props == None) or (self.props == {}):
            return ""
        return "".join(f' {k}="{v}"' for k, v in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode({self.tag!r}, {self.value!r}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return(f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")
    
    def __repr__(self):
        return f"HTMLNode({self.tag!r}, {self.value!r}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if not self.children:
            raise ValueError("All parent nodes must have children")
        children_result = ""
        for child in self.children:
            children_result += child.to_html()
        return(f"<{self.tag}{self.props_to_html()}>{children_result}</{self.tag}>")
    

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("Invalid text node type")