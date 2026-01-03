import unittest
from textnode import TextNode, TextType
from split_nodes_link import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
    def test_empty_list(self):
        result = split_nodes_link([])
        self.assertEqual(result, [])

    def test_no_links(self):
        result = split_nodes_link([TextNode("hello world", TextType.TEXT)])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "hello world")

    def test_single_link(self):
        nodes = [TextNode("check [this](https://example.com) out", TextType.TEXT)]
        result = split_nodes_link(nodes)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "check ")
        self.assertEqual(result[1].text, "this")
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[1].url, "https://example.com")
        self.assertEqual(result[2].text, " out")

    def test_link_at_start(self):
        nodes = [TextNode("[link](https://example.com) text", TextType.TEXT)]
        result = split_nodes_link(nodes)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "link")
        self.assertEqual(result[0].text_type, TextType.LINK)
        self.assertEqual(result[1].text, " text")

    def test_link_at_end(self):
        nodes = [TextNode("text [link](https://example.com)", TextType.TEXT)]
        result = split_nodes_link(nodes)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "text ")
        self.assertEqual(result[1].text, "link")
        self.assertEqual(result[1].text_type, TextType.LINK)

    def test_multiple_links(self):
        nodes = [TextNode("text [link1](https://example.com) middle [link2](https://test.com) end", TextType.TEXT)]
        result = split_nodes_link(nodes)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[3].text_type, TextType.LINK)

    

if __name__ == "__main__":
    unittest.main()


   