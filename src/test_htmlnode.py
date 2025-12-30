import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        self.assertEqual(node.props_to_html(),'style="color:red" aria-label="paragraph" ')
        
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
        
        
        
        
        
    
    
        


if __name__ == "__main__":
    unittest.main()