import os


from markdown_to_html import *
from htmlnode import *


def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            title = line.lstrip("#").strip()
            return title
    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as file:
        from_contents = file.read()
    with open(template_path) as file:
        template_contents = file.read()

    from_html_node = markdown_to_html_node(from_contents)
    from_html_string = from_html_node.to_html()

    title = extract_title(from_contents)
    
    full_page = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", from_html_string)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
        
    with open(dest_path, "w") as file:
        file.write(full_page)