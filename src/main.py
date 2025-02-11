import os
import shutil
from copystatic import copy_directory_to_destination
from generatecontent import generate_pages_recursive

content_dir_path = "./content"
template_path = "./template.html"
public_dir_path = "./public"
static_dir_path = "./static"

def main():
    print("Deleting public directory...")
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)

    print("Copying static files to public directory...")

    copy_directory_to_destination(static_dir_path, public_dir_path)


    print("Generating content...")
    generate_pages_recursive(content_dir_path, template_path, public_dir_path)
main()