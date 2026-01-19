from textnode import BlockType
import re

def block_to_block_type(block):
    lines = block.splitlines()
    non_empty = [line for line in lines if line.strip()]
    
    if not non_empty:
        return BlockType.PARAGRAPH
    
    # Check heading (only first line needs to match)
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    
    # Check code block
    lines = block.split("\n")
    if len(lines) >= 2 and lines[0].strip() == "```" and lines[-1].strip() == "```":
        return BlockType.CODE
    
    # Check if ALL lines start with "> "
    if all(line.lstrip().startswith(">") for line in non_empty):
        return BlockType.QUOTE
    
    # Check if ALL lines start with "- "
    if all(line.startswith("- ") for line in non_empty):
        return BlockType.UNORDERED_LIST
    
    # Check ordered list with sequential numbering
    is_ordered = True
    expected_number = 1
    for line in non_empty:
        if not line.startswith(f"{expected_number}. "):
            is_ordered = False
            break
        expected_number += 1
    
    if is_ordered:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
  

def is_ordered_list(block):
    lines = block.splitlines()
    
    # Don't filter out empty lines - they should break the list format
    if not lines:
        return False
    
    expected_number = 1
    for line in lines:
        # Check if line starts with expected number followed by ". "
        if not line.startswith(f"{expected_number}. "):
            return False
        expected_number += 1
    
    return True



    
    

