import sys
import re
from pydantic import ValidationError
from schema import structure_base 
#declaration of a funtion to check for the irregularities in each structured input

def parse_messy_line(raw_line: str) -> dict | None:
    """Parses a single messy string into a validated dictionary."""
    if not raw_line.strip():
        return None
        
    # Split by either pipe '|' or semicolon ';'
    parts = re.split(r'[|;]', raw_line)
    
    raw_dict = {}
    for part in parts:
        if '=' in part:
            key, value = part.split('=', 1)
            raw_dict[key.strip().lower()] = value.strip()
            
    try:
        # Pass the raw dictionary to Pydantic for strict validation
        validated_record = structure_base(**raw_dict)
        return validated_record.model_dump()
        
    except ValidationError as e:
        # Extract friendly error messages
        errors = [f"{err['loc'][0]}: {err['msg']}" for err in e.errors()]
        sys.stderr.write(f"[WARNING] Skipping line due to errors {errors}. Line: '{raw_line}'\n")
        return None