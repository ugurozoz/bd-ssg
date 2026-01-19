import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_single_h1(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extract_title_with_content_after(self):
        markdown = "# My Title\n\nSome content here"
        self.assertEqual(extract_title(markdown), "My Title")

    def test_extract_title_with_content_before(self):
        markdown = "## Subtitle\n# Main Title\nContent"
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_extract_title_with_extra_spaces(self):
        markdown = "#   Spaced Title   "
        self.assertEqual(extract_title(markdown), "Spaced Title")

    def test_extract_title_no_h1_raises_exception(self):
        markdown = "## Subtitle\n### Another subtitle"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No h1 header found")

    def test_extract_title_empty_h1(self):
        markdown = "# "
        self.assertEqual(extract_title(markdown), "")

    def test_extract_title_empty_string_raises_exception(self):
        markdown = ""
        with self.assertRaises(Exception):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()