import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextnodes(unittest.TestCase):
    
    def test_text_with_bold(self):
        text = "This is **bold** text"
        result = text_to_textnodes(text)
        self.assertIsNotNone(result)
    
    def test_text_with_italic(self):
        text = "This is _italic_ text"
        result = text_to_textnodes(text)
        self.assertIsNotNone(result)
    
    def test_text_with_code(self):
        text = "This is `code` text"
        result = text_to_textnodes(text)
        self.assertIsNotNone(result)
    
    def test_text_with_image(self):
        text = "![alt](https://example.com/image.png)"
        result = text_to_textnodes(text)
        self.assertIsNotNone(result)
    
    def test_text_with_link(self):
        text = "[link text](https://example.com)"
        result = text_to_textnodes(text)
        self.assertIsNotNone(result)
    
    def test_mixed_formatting(self):
        text = "This is **bold** and _italic_ with `code`"
        result = text_to_textnodes(text)
        self.assertIsNotNone(result)
    
    def test_complex_sample_text(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertEqual(result,[
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ])
        
    def test_complex_mixed_content(self):
        text = "See **docs** at [site](url) or ![img](imgurl) then use `npm install`."
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("See ", TextType.TEXT),
            TextNode("docs", TextType.BOLD),
            TextNode(" at ", TextType.TEXT),
            TextNode("site", TextType.LINK, "url"),
            TextNode(" or ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "imgurl"),
            TextNode(" then use ", TextType.TEXT),
            TextNode("npm install", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ])
    
    def test_plain_text(self):
        text = "This is plain text"
        result = text_to_textnodes(text)
        self.assertIsNotNone(result)
    
    
    def test_multiline_three_lines_longer_no_nested(self):
        text = """First line has **bold text**, an _italic word_, and `inline code`, followed by more plain text to increase length and realism. Second line includes a [link](https://example.com) and an image ![img](https://img.com/a.png), plus extra descriptive words that stay unformatted and simple. Third line ends with **bold**, _italic_, and `code` only, then continues with additional normal text to ensure longer parsing paths."""

        result = text_to_textnodes(text)

        self.assertEqual(result, [
            TextNode("First line has ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(", an ", TextType.TEXT),
            TextNode("italic word", TextType.ITALIC),
            TextNode(", and ", TextType.TEXT),
            TextNode("inline code", TextType.CODE),
            TextNode(", followed by more plain text to increase length and realism. Second line includes a ", TextType.TEXT),

            
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and an image ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "https://img.com/a.png"),
            TextNode(", plus extra descriptive words that stay unformatted and simple. Third line ends with ", TextType.TEXT),

            
            TextNode("bold", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" only, then continues with additional normal text to ensure longer parsing paths.", TextType.TEXT),
        ])

    
    
   




if __name__ == "__main__":
    unittest.main()