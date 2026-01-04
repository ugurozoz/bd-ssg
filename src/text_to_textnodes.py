from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from delimiter import split_nodes_delimiter, delimiter_to_type
from textnode import TextNode, TextType


sample_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

def text_to_textnodes(text):
    
    text_node = TextNode(text, TextType.TEXT)
    nodes = [text_node]
    for dlm in ['`','**','_']:
        nodes = split_nodes_delimiter(nodes,dlm, delimiter_to_type(dlm))
        #print(">>",nodes ,'\n')
    nodes_with_images = split_nodes_image(nodes)
    nodes_with_links_and_images = split_nodes_link(nodes_with_images)
    #print('NODES WITH IMAGES',nodes_with_images)
    for node in nodes_with_links_and_images:
        pass
        #print('NODE >> : ', node, '\n')
    
    #print('>>>>',nodes_with_links_and_images)
    return nodes_with_links_and_images





    
def main():
    text_to_textnodes(sample_text)
    
    
if __name__ == "__main__":
    main()