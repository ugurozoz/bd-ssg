import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    
    def test_nones(self):
        node = HTMLNode()
        self.assertTrue(
            node.tag == None and node.value == None
        )
        
        
    def test_props_to_html(self):
        node = HTMLNode(
            'p',
            'This is a paragraph',
            ['span','b'],
            {
                'style':'color:red',
                'aria-label':'paragraph'
             }
        )
        self.assertEqual(node.props_to_html(),' style="color:red" aria-label="paragraph"')
        
    def test_tag(self):
        node = HTMLNode('span')
        self.assertIsInstance(node.tag, (str, type(None)))
    
    def test_value(self):
        node = HTMLNode('span','This text is in a span')
        self.assertEqual(node.value, 'This text is in a span')
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
        
        
        
        
    
    
        


if __name__ == "__main__":
    unittest.main()