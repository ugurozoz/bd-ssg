import unittest
from extract_links import extract_markdown_links

class TestHTMLNode(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_markdown_links_empty_string(self):
        matches = extract_markdown_links("")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_no_links(self):
        matches = extract_markdown_links("This is text without any links")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_single_link(self):
        matches = extract_markdown_links("Check out [my site](https://example.com)")
        self.assertListEqual([("my site", "https://example.com")], matches)

    def test_extract_markdown_links_with_special_characters(self):
        matches = extract_markdown_links("[link-text_123](https://example.com/path?query=1&other=2)")
        self.assertListEqual([("link-text_123", "https://example.com/path?query=1&other=2")], matches)
        
        
if __name__ == "__main__":
    unittest.main()
    
    
