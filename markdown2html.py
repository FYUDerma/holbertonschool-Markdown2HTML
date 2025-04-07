#!/usr/bin/python3
"""
markdown2html.py

This script converts a Markdown file into an HTML file. It takes two arguments:
1. The input Markdown file (e.g., README.md).
2. The output HTML file (e.g., README.html).

Usage:
    ./markdown2html.py input_file.md output_file.html

The script checks if the input file exist and write the converted HTML content
to the specified output file. If the input file is missing or the arguments are
incorrect, it exits with an error message.
"""
import sys
import os


def convert_markdown_to_html(markdown_text):
    """Convert Markdown text to HTML."""
    html_lines = []
    lines = markdown_text.splitlines()
    
    for line in lines:
        line = line.strip()
        """Convert Markdown links to HTML links."""
        if line.startswith('#'):
            """
            Convert Markdown headers to HTML headers.
            The number of '#' characters indicates the header level.
            """
            level = len(line) - len(line.lstrip('#'))
            content = line.lstrip('#').strip()
            html_lines.append(f"<h{level}>{content}</h{level}>")
    return "\n".join(html_lines)

def main():
    """
    Main function to handle Markdown to HTML conversion.
    """

    if len(sys.argv) < 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    try:
        with open(input_file, 'r') as f:
            markdown_text = f.read()
        html_output = convert_markdown_to_html(markdown_text)

        with open(output_file, 'w') as f:
            f.write(html_output)
        
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
