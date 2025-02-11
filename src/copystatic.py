import os
import shutil
def get_directory_contents(dir, content_list):
    contents = content_list
    current_level = os.listdir(dir)
    for child in current_level:
        child_path = dir + "/" + child
        if os.path.isfile(child_path):
            contents.append(child_path)
        else:
            get_directory_contents(child_path, contents)
    return contents

def copy_directory_to_destination(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    if os.path.exists(source_dir):
        paths_to_copy = get_directory_contents(source_dir, [])
        for path in paths_to_copy:
            replaced = path.replace(source_dir, dest_dir)
            parent_dir = os.path.dirname(replaced)
            if os.path.isdir(parent_dir):
                try:
                    shutil.copy(path, replaced)
                except Exception as e:
                    print("didn't copy, error: {e}")
            else:
                os.mkdir(parent_dir)
                try:
                    shutil.copy(path, replaced)
                except Exception as e:
                    print("didn't copy, error: {e}")

    else:
        print("source path not found")