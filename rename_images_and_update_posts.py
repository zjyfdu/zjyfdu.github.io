import os
import re

IMAGE_DIR = '/Users/bytedance/zjyfdu.github.io/source/images/'
POST_DIR = '/Users/bytedance/zjyfdu.github.io/source/_posts/'

def rename_images():
    """Renames images in the IMAGE_DIR by removing spaces from their filenames."""
    renamed_files = {}
    for filename in os.listdir(IMAGE_DIR):
        if ' ' in filename:
            new_filename = filename.replace(' ', '')
            old_path = os.path.join(IMAGE_DIR, filename)
            new_path = os.path.join(IMAGE_DIR, new_filename)
            try:
                os.rename(old_path, new_path)
                renamed_files[filename] = new_filename
                print(f'Renamed: "{filename}" to "{new_filename}"')
            except OSError as e:
                print(f'Error renaming "{filename}": {e}')
    return renamed_files

def update_markdown_files(renamed_files):
    """Updates image links in markdown files in POST_DIR."""
    if not renamed_files:
        print("No files were renamed, so no markdown files to update.")
        return

    for post_filename in os.listdir(POST_DIR):
        if post_filename.endswith('.md'):
            post_path = os.path.join(POST_DIR, post_filename)
            try:
                with open(post_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content

                for old_image_name, new_image_name in renamed_files.items():
                    # Regex to find markdown image links like ![](/images/name with space.png)
                    # and also plain links like (/images/name with space.png)
                    # It handles URL encoding of spaces (%20) as well.
                    old_image_name_escaped = re.escape(old_image_name)
                    old_image_name_url_encoded = old_image_name.replace(' ', '%20')
                    old_image_name_url_encoded_escaped = re.escape(old_image_name_url_encoded)
                    
                    # Pattern for ![](/images/...) or [](/images/...)
                    pattern1 = r'(!\[[^\]]*\]\s*\()(\s*/images/)(' + old_image_name_escaped + r')(\s*\))'
                    content = re.sub(pattern1, r'\1\2' + new_image_name + r'\4', content)
                    pattern2 = r'(!\[[^\]]*\]\s*\()(\s*/images/)(' + old_image_name_url_encoded_escaped + r')(\s*\))'
                    content = re.sub(pattern2, r'\1\2' + new_image_name + r'\4', content)

                    # Pattern for plain links (/images/...)
                    pattern3 = r'(\()(\s*/images/)(' + old_image_name_escaped + r')(\s*\))'
                    content = re.sub(pattern3, r'\1\2' + new_image_name + r'\4', content)
                    pattern4 = r'(\()(\s*/images/)(' + old_image_name_url_encoded_escaped + r')(\s*\))'
                    content = re.sub(pattern4, r'\1\2' + new_image_name + r'\4', content)
                    
                    # Pattern for src="/images/..."
                    pattern5 = r'(src=")(\s*/images/)(' + old_image_name_escaped + r')(")'
                    content = re.sub(pattern5, r'\1\2' + new_image_name + r'\4', content)
                    pattern6 = r'(src=")(\s*/images/)(' + old_image_name_url_encoded_escaped + r')(")'
                    content = re.sub(pattern6, r'\1\2' + new_image_name + r'\4', content)

                if original_content != content:
                    with open(post_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f'Updated image links in: "{post_filename}"')
            except Exception as e:
                print(f'Error processing "{post_filename}": {e}')

if __name__ == '__main__':
    print("Starting image renaming process...")
    renamed_image_files = rename_images()
    print("\nStarting markdown file update process...")
    update_markdown_files(renamed_image_files)
    print("\nScript finished.")