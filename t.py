import os
from nbconvert import MarkdownExporter
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat

def convert_ipynb_to_md(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".ipynb"):
            input_path = os.path.join(directory, filename)
            output_path = os.path.splitext(input_path)[0] + ".md"

            exporter = MarkdownExporter()
            exporter.register_preprocessor(ExecutePreprocessor(timeout=600), True)

            with open(input_path, 'r', encoding='utf-8') as notebook_file:
                notebook_content = notebook_file.read()
                notebook_content = nbformat.reads(notebook_content, as_version=4)
                md_content, _ = exporter.from_notebook_node(notebook_content)

            with open(output_path, 'w', encoding='utf-8') as md_file:
                md_file.write(md_content)

            print(f"Converted {filename} to Markdown")

convert_ipynb_to_md(os.getcwd())
