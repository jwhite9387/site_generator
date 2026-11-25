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

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as file:
        from_contents = file.read()
    with open(template_path) as file:
        template_contents = file.read()

    from_html_node = markdown_to_html_node(from_contents)
    from_html_string = from_html_node.to_html()

    title = escape(extract_title(from_contents), quote=False)
    
    full_page = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", from_html_string)
    full_page = full_page.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
        
    with open(dest_path, "w") as file:
        file.write(full_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_path_items = os.listdir(dir_path_content)
    for item in dir_path_items:
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isdir(content_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            generate_pages_recursive(content_path, template_path, dest_path, basepath)
        elif os.path.isfile(content_path) and content_path.endswith(".md"):
            html_page = dest_path.replace(".md", ".html")
            generate_page(content_path, template_path, html_page, basepath)