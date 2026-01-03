from src.textnode import TextNode, TextType




def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #print('OLD NODES',old_nodes)
    new_nodes = []
    for node in old_nodes:
        #print('NODE', node)
        if node.text.count(delimiter) == 0:
            new_nodes.append(node)
                        
            continue
        if node.text == delimiter:
            raise Exception('Delimiter only')
        parts = node.text.split(delimiter)
        
        if len(parts) % 2 == 0:
            raise Exception('Unmatched delimiters')
        if delimiter_to_type(delimiter) == node.text_type:
            new_nodes.append(node)
            continue
        
        # subroutine
        index = 0
        
        for part in parts:
            if part != '':
                new_node = TextNode(part, TextType.TEXT)
                if index % 2 == 1:                
                        new_node.text_type = delimiter_to_type(delimiter)                    
                new_nodes.append(new_node)
            index += 1
    #print('NEW NODES', new_nodes)      
    return new_nodes
        
    
    def build_node(text, type):
        return TextNode(text, type)


def delimiter_to_type(delimiter):
    match delimiter:
        case '`':
            return TextType.CODE
        case '**':
            return TextType.BOLD
        case '_':
            return TextType.ITALIC
        case _:
            return TextType.TEXT
        