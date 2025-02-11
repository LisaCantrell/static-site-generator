import os
from block_markdown import markdown_to_html_node, extract_title
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generaging page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as fp:
        from_contents = fp.read()
    
    with open(template_path) as tp:
        template_contents = tp.read()
    
    converted_html_node = markdown_to_html_node(from_contents)
    html_string = converted_html_node.to_html()

    title = extract_title(from_contents)
    template_contents = template_contents.replace("{{ Title }}", title)
    template_contents = template_contents.replace("{{ Content }}", html_string)

    dest_path_dir = os.path.dirname(dest_path)
    if dest_path_dir != "":
        os.makedirs(dest_path_dir, exist_ok=True)
        to_file = open(dest_path, "w")
        to_file.write(template_contents)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):    
    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)            
        else:
            # os.mkdir(new_dir_path)
            generate_pages_recursive(from_path, template_path, dest_path)


# content_path = "./content"
# tem_path = "./template.html"
# dest_path = "./public"
# generate_pages_recursive(content_path, tem_path, dest_path)