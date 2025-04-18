#!/usr/bin/python3
"""
markdown2html.py

This script converts a Markdown file into an HTML file. It takes two arguments:
1. The input Markdown file (e.g., README.md).
2. The output HTML file (e.g., README.html).

Usage:
    ./markdown2html.py input_file.md output_file.html

Case:
    - Unordered list
    - Ordered list
    - Headers

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

    # Flags variables
    unorganize_list = False
    organize_list = False
    paragraph_flag = False

    for line in lines:
        line = line.strip()

        """
        If the line starts with '-', it is considered an unordered list item.
        """
        if line.startswith('-'):
            if not unorganize_list:
                html_lines.append("<ul>")
                unorganize_list = True
            item = line.lstrip('-').strip()
            html_lines.append(f"<li>{item}</li>")
        else:
            if unorganize_list:
                html_lines.append("</ul>")
                unorganize_list = False

        """
        If the line starts with '*', it is considered an ordered list item.
        """
        if line.startswith('*'):
            if not organize_list:
                html_lines.append("<ol>")
                organize_list = True
            item = line.lstrip('*').strip()
            html_lines.append(f"<li>{item}</li>")
        else:
            if organize_list:
                html_lines.append("</ol>")
                organize_list = False

        """
        If the line starts with '#', it is considered a header.
        The number of '#' characters indicates the header level.
        """
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            content = line.lstrip('#').strip()
            html_lines.append(f"<h{level}>{content}</h{level}>")

        """
        if the line starts with no character, it is considered a paragraph.
        if there is two line without any special character, a <br/> is added.
        """
        if line and not line.startswith(('-', '*', '#')):
            if not paragraph_flag:
                html_lines.append("<p>")
                paragraph_flag = True
            else:
                html_lines.append("<br/>")
            html_lines.append(line)
        elif line == "":
            if paragraph_flag:
                html_lines.append("</p>")
                paragraph_flag = False

    if unorganize_list:
        html_lines.append("</ul>")
    if organize_list:
        html_lines.append("</ol>")
    if paragraph_flag:
        html_lines.append("</p>")


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
