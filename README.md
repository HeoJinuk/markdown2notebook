# Markdown to Jupyter Notebook Converter

This script converts a Markdown (`.md`) file into a Jupyter Notebook (`.ipynb`) file.

## Requirements

This script requires Python and the `nbformat` library.

Install the required library using:

```sh
pip install nbformat
```

## Usage

Run the script using the following command:

```sh
python script.py <input_markdown_file> <output_notebook_file>
```

### Example:

```sh
python script.py example.md example.ipynb
```

## How It Works

1. Reads the Markdown content from the input file.
2. Creates a new Jupyter Notebook (`.ipynb`) file.
3. Adds the Markdown content as a Markdown cell in the notebook.
4. Saves the notebook as the output file.

## License

This project is licensed under the MIT License.

