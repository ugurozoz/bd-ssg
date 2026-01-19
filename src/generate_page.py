import os
from markdown_to_html_node import markdown_to_html_node
import shutil
from extract_title import extract_title
from pathlib import Path


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = ''
    template = ''
    with open(from_path, encoding="utf-8") as f:
        md = f.read()
    html_node = markdown_to_html_node(md)
    html = html_node.to_html()
    with open(template_path, encoding="utf-8") as f:
        template = f.read()
    
    title = extract_title(md)
    result = template.replace("{{ Title }}",title)
    result = result.replace("{{ Content }}", html)
    
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(result)
    
    
    
    
    #print("TITLE:::",title)
    #print("TEMPLATE",result)
    


