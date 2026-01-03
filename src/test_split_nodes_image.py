import unittest
from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image


class TestSplitNodesImage(unittest.TestCase):
    
    def test_01_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_02_split_images_no_images(self):
        node = TextNode("This is text without any images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is text without any images", TextType.TEXT)],
            new_nodes,
        )

    def test_03_split_images_empty_list(self):
        new_nodes = split_nodes_image([])
        self.assertListEqual([], new_nodes)

    def test_04_split_images_single_image(self):
        node = TextNode("Check this ![alt text](https://example.com/img.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Check this ", TextType.TEXT),
                TextNode("alt text", TextType.IMAGE, "https://example.com/img.png"),
            ],
            new_nodes,
        )
    
    def test_05_split_images_image_at_start(self):
        node = TextNode("![image](https://example.com/img.png) and text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://example.com/img.png"),
                TextNode(" and text", TextType.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()