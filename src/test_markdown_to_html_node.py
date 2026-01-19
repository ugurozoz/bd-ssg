import unittest
from markdown_to_html_node import markdown_to_html_node
from htmlnode import ParentNode, LeafNode

class TestMarkdownToHtmlNode(unittest.TestCase):
    
    def test_paragraph(self):
        md = "This is a paragraph"
        result = markdown_to_html_node(md)
        self.assertIsInstance(result, ParentNode)
        self.assertEqual(result.tag, "div")
        self.assertTrue(len(result.children) > 0)
    
    def test_heading(self):
        md = "# Heading 1"
        result = markdown_to_html_node(md)
        self.assertEqual(result.tag, "div")
        self.assertEqual(result.children[0].tag, "h1")
    
    def test_multiple_headings(self):
        md = "# H1\n\n## H2\n\n### H3"
        result = markdown_to_html_node(md)
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 3)
        self.assertEqual(result.children[0].tag, "h1")
        self.assertEqual(result.children[1].tag, "h2")
        self.assertEqual(result.children[2].tag, "h3")
    
    def test_code_block(self):
        md = "```\ncode here\n```"
        result = markdown_to_html_node(md)
        self.assertEqual(result.children[0].tag, "pre")
    
    def test_quote_block(self):
        md = "> This is a quote\n> continued quote"
        result = markdown_to_html_node(md)
        self.assertEqual(result.children[0].tag, "blockquote")
    
    def test_unordered_list(self):
        md = "- Item 1\n- Item 2\n- Item 3"
        result = markdown_to_html_node(md)
        self.assertEqual(result.children[0].tag, "ul")
    
    def test_ordered_list(self):
        md = "1. Item 1\n2. Item 2\n3. Item 3"
        result = markdown_to_html_node(md)
        self.assertEqual(result.children[0].tag, "ol")
    
    def test_mixed_content(self):
        md = "# Heading\n\nParagraph text\n\n- List item"
        result = markdown_to_html_node(md)
        self.assertEqual(result.tag, "div")
        self.assertGreaterEqual(len(result.children), 3)
    def test_markdown_to_html_paragraphs(self):
        md = """
    This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_markdown_to_html_heading_and_paragraph(self):
        md = """
    # Heading level 1

    This is a simple paragraph with some text in it.
It has no special prefix and should be parsed as a paragraph.
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading level 1</h1>"
            "<p>This is a simple paragraph with some text in it. "
            "It has no special prefix and should be parsed as a paragraph.</p></div>",
        ) 
        
    def test_markdown_to_html_blockquote(self):
        md = """
    > This is a quote line
> that continues on the next line.
> And even a third line.
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote line that continues on the next line. "
            "And even a third line.</blockquote></div>",
        )
        
    def test_markdown_to_html_lists(self):
        md = """
    - First bullet
- Second bullet with _italic_ text
- Third bullet with **bold** text

    1. First item
2. Second item with **bold** text
3. Third item with _italic_ text
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<ul>"
            "<li>First bullet</li>"
            "<li>Second bullet with <i>italic</i> text</li>"
            "<li>Third bullet with <b>bold</b> text</li>"
            "</ul>"
            "<ol>"
            "<li>First item</li>"
            "<li>Second item with <b>bold</b> text</li>"
            "<li>Third item with <i>italic</i> text</li>"
            "</ol>"
            "</div>",
        )
    
    


if __name__ == "__main__":
    unittest.main()