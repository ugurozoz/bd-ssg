import unittest
from src.delimiter import split_nodes_delimiter
from src.textnode import TextNode, TextType





class TestHTMLNode(unittest.TestCase):

    # ----------------
    # Basic cases
    # ----------------
    
    def test_01_single_delimiter(self):
        nodes = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)

        self.assertEqual(result, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])
    
   
    def test_02_multiple_delimiters(self):
        nodes = [TextNode("Here is `code` and more `inline` code", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)

        self.assertEqual(result, [
            TextNode("Here is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and more ", TextType.TEXT),
            TextNode("inline", TextType.CODE),
            TextNode(" code", TextType.TEXT),
        ])
    
    
    def test_03_delimiter_at_start(self):
        nodes = [TextNode("`start` of the sentence", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)

        self.assertEqual(result, [
            TextNode("start", TextType.CODE),
            TextNode(" of the sentence", TextType.TEXT),
        ])
    
    def test_04_delimiter_at_end(self):
        nodes = [TextNode("end of the sentence with `code`", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)

        self.assertEqual(result, [
            TextNode("end of the sentence with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ])
    
    # ----------------
    # Edge cases
    # ----------------

    def test_05_no_delimiters(self):
        nodes = [TextNode("plain text without formatting", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)

        self.assertEqual(result, nodes)
    
    
    
   
    
    def test_08_multiple_nodes_mixed(self):
        nodes = [
            TextNode("first with `code`", TextType.TEXT),
            TextNode("second without", TextType.TEXT),
            
            TextNode("another `snippet` here", TextType.TEXT),
        ]

        result = split_nodes_delimiter(nodes, "`", TextType.CODE)

        self.assertEqual(result, [
            TextNode("first with ", TextType.TEXT),
            TextNode("code", TextType.CODE),

            TextNode("second without", TextType.TEXT),

            

            TextNode("another ", TextType.TEXT),
            TextNode("snippet", TextType.CODE),
            TextNode(" here", TextType.TEXT),
        ])

    # ----------------
    # Error cases
    # ----------------
    
    def test_09_unmatched_opening_delimiter(self):
        nodes = [TextNode("this has an `unclosed code block", TextType.TEXT)]

        with self.assertRaises(Exception):
            split_nodes_delimiter(nodes, "`", TextType.CODE)

    def test_10_single_delimiter_only(self):
        nodes = [TextNode("`", TextType.TEXT)]

        with self.assertRaises(Exception):
            split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # ----------------
    # Different delimiters
    # ----------------
    
    def test_11_bold_double_asterisk(self):
        nodes = [TextNode("this is **bold text** example", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        self.assertEqual(result, [
            TextNode("this is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" example", TextType.TEXT),
        ])

    def test_12_italic_single_underscore(self):
        nodes = [TextNode("this is _italic text_ example", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

        self.assertEqual(result, [
            TextNode("this is ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" example", TextType.TEXT),
        ])
        
        
        
if __name__ == "__main__":
    unittest.main()
 
        