#!/usr/bin/env python3
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


def main():
    """
    Main function to handle Markdown to HTML conversion.
    """
    # Check if the number of arguments is correct
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Input and output file variables
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Placeholder for Markdown to HTML conversion logic
    # (To be implemented)

    sys.exit(0)


if __name__ == "__main__":
    main()
