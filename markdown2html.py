#!/usr/bin/env python3
# Transform an Readme.md file into a HTML file
import sys
import os

def main(*args, **kwargs):
    # Check if the number of arguments is correct
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit (1)

    # Input and output file variables
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        exit (1)
    
    exit(0)

if __name__ == "__main__":
    main()
