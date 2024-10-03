from parse_data import parse

import os

# Define a function to read and parse files based on their extension
def parse_files(file_list):
    for file_name in file_list:
        with open(file_name, 'r') as file:
            content = file.read()

        # Determine file type based on the extension
        if file_name.endswith('.json'):
            parser = parse(content)
            parser.parse('json')
        elif file_name.endswith('.xml'):
            parser = parse(content)
            parser.parse('xml')
        elif file_name.endswith('.yaml') or file_name.endswith('.yml'):
            parser = parse(content)
            parser.parse('yaml')
        else:
            print(f"Unsupported file format: {file_name}")

# List of files to parse
files_to_parse = [
    'data.json',  # Replace with your actual JSON file
    'data.yaml',  # Replace with your actual YAML file
    'data.xml'    # Replace with your actual XML file
]

# Call the function to parse the files
parse_files(files_to_parse)
