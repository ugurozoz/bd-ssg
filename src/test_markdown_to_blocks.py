
import unittest
from markdown_to_blocks import markdown_to_blocks
from textnode import TextNode, TextType

class TestSplitNodesImage(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        def test_leading_and_trailing_blank_lines(self):
            md = """

First paragraph

Second paragraph

"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
        blocks,
        [
            "First paragraph",
            "Second paragraph",
        ],
    )
        def test_multiple_blank_lines(self):
            md = """
Paragraph one


Paragraph two



Paragraph three
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
        blocks,
        [
            "Paragraph one",
            "Paragraph two",
            "Paragraph three",
        ],
    )
        def test_single_paragraph_multiline(self):
            md = """
Line one
Line two
Line three
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
        blocks,
        [
            "Line one\nLine two\nLine three",
        ],
    )
            
        def test_paragraph_and_list(self):
            md = """
Intro paragraph

- item one
- item two
- item three
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
        blocks,
        [
            "Intro paragraph",
            "- item one\n- item two\n- item three",
        ],
    )
            
        def test_list_split_by_blank_line(self):
            md = """
- item one

- item two
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
        blocks,
        [
            "- item one",
            "- item two",
        ],
    )
            
        def test_code_inside_paragraph(self):
            md = """
This paragraph has `inline code`
and continues on the next line
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
        blocks,
        [
            "This paragraph has `inline code`\nand continues on the next line",
        ],
    )
        def test_empty_input(self):
            md = ""
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])
        
        def test_whitespace_only_input(self):
            md = "   \n\n   "
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])

        
if __name__ == "__main__":
    unittest.main()