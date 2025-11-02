import os
 
def rename_index_to_readme(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'index.md':
                index_path = os.path.join(dirpath, filename)
                readme_path = os.path.join(dirpath, 'README.md')
                os.rename(index_path, readme_path)
                print(f'Umbenannt: {index_path} -> {readme_path}')
 
if __name__ == "__main__":
    current_directory = os.getcwd()
    rename_index_to_readme(current_directory)
 