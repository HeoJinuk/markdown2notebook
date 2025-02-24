import argparse
import nbformat
import re


def convert_to_ipynb(input_file, output_file):
    """
    Converts a Markdown file to a Jupyter Notebook file, splitting content into separate cells.
    """
    # Read the Markdown file
    with open(input_file, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Split content into cells based on Markdown headers (##)
    sections = re.split(r"(#+ .*)", markdown_content)

    # Create a new Jupyter Notebook object
    notebook = nbformat.v4.new_notebook()

    for section in sections:
        section = section.strip()
        
        if not section:
            continue
        
        # Convert code blocks into code cells
        if section.startswith("```"):
            code_content = section.strip("```").strip()
            code_content = "\n".join(code_content.split("\n")[1:])
            notebook.cells.append(nbformat.v4.new_code_cell(code_content))
        else:
            # Otherwise, treat it as Markdown
            notebook.cells.append(
                nbformat.v4.new_markdown_cell(section))

    # Save the Jupyter Notebook file
    with open(output_file, "w", encoding="utf-8") as f:
        nbformat.write(notebook, f)


if __name__ == "__main__":
    # Set up the command-line interface
    parser = argparse.ArgumentParser(
        description="Convert a Markdown file to a structured Jupyter Notebook file.")
    parser.add_argument("input_file", help="The input Markdown file path")
    parser.add_argument(
        "output_file", help="The output Jupyter Notebook file path")
    args = parser.parse_args()

    # Execute the conversion
    convert_to_ipynb(args.input_file, args.output_file)
