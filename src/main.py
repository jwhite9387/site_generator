import shutil
import os
import sys

from textnode import TextType, TextNode
from htmlnode import HTMLNode
from gencontent import *

def main():
    text_node = TextNode("some text", TextType.LINK, "https://example.com")
    print(text_node)
    html_node = HTMLNode("a", "paragraph text", [], {"href": "https://google.com", "target": "_blank"})
    print(html_node)
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
    prep_and_copy("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)
    
    
def copy_content(src, dest):
    for name in os.listdir(src):
        full_src_path = os.path.join(src, name)
        full_dest_path = os.path.join(dest, name)

        if os.path.isfile(full_src_path):
            print(f"Copying {full_src_path} -> {full_dest_path}")
            shutil.copy(full_src_path, full_dest_path)
        elif os.path.isdir(full_src_path):
            os.mkdir(full_dest_path)
            copy_content(full_src_path, full_dest_path)

def prep_and_copy(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    if not os.path.isdir(src):
        raise Exception("Source path is not a directory")
    os.mkdir(dest)
    copy_content(src, dest)

main()