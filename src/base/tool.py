r"""Tools
"""
import json
import os



def to_prase_json(filePath: str) -> dict:
        with open(filePath, 'r') as file:
            data: dict = json.load(file)
            
        return data
    
    
def auto_load_css(window):
    css_dir = "./static/css"
    for file in os.listdir(css_dir):
        if file.endswith('.css'):
            css_file_path = os.path.join(css_dir, file)
            with open(css_file_path, 'r') as f:
                css_content = f.read() 
            window.load_css(css_content)
                