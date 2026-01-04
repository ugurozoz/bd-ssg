from textnode import TextNode, TextType
from extract_images import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []
    if len(old_nodes) == 0:
        return []
    for node in old_nodes:
        if node.text_type in [TextType.BOLD, TextType.ITALIC, TextType.CODE, TextType.LINK]:
            new_nodes.append(node)
            continue          
        matches = extract_markdown_images(node.text)
        if matches == None and node.text != '':
            new_nodes.append(TextNode(node.text,node.text_type)) 
            continue
        text = node.text
        for match in matches:
                       
            text_to_process = text.split(f'![{match[0]}]({match[1]})',1)
            if text_to_process[0] != '':
                
                new_nodes.append(TextNode(text_to_process.pop(0),TextType.TEXT))
            else:
                #print('ZERO LENGTH TEXT!!!')
                #print('TEXT >>', text)
                text_to_process.pop(0)
            new_nodes.append(TextNode(f"{match[0]}", TextType.IMAGE, f"{match[1]}"),)
            
            text = text_to_process[0]
        
        if text != "":
            #print('LAST ACT >>>', text)
            new_nodes.append(TextNode(text,TextType.TEXT))    
    #print('NEW NODES',new_nodes)        
    return new_nodes