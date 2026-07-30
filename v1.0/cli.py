""" this is the CLI design of the whole program """
import sys
import json
import typer
from typing import Optional
from engine import parse_messy_line

app = typer.Typer(help="A production-grade CLI parser for messy log files.")

@app.command()
def process(
    input_file: typer.FileText = typer.Argument(
        ..., 
        help="Path to the messy log file. Use '-' to read from standard input."
    ),
):
    """
    Reads raw text data, extracts fields, and outputs structured JSON to standard output.
    """
    sys.stderr.write("[INFO] Starting parser...\n")
    
    print("[")  # Start JSON array
    first_item = True
     
    # Read line-by-line to handle massive files without crashing memory
    for line in input_file:
        parsed_data = parse_messy_line(line)
        
        if parsed_data:
            if not first_item:
                print(",")
                
            # Serialize to JSON and print to stdout
            print(json.dumps(parsed_data, indent=4), end="")
            first_item = False
            
    print("\n]") # End JSON array
    sys.stderr.write("[INFO] Parsing complete.\n")

if __name__ == "__main__":
    app()