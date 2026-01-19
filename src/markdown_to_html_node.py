from markdown_to_blocks import markdown_to_blocks, extract_code_text
#from ____block_to_textnodes import block_to_textnodes
from block_to_block_type import block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import BlockType
from htmlnode import text_node_to_html_node


md = """

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here


# This is h1 header

## This is h2 header

### This is h3 header 

# Heading level 1

This is a simple paragraph with some text in it.
It has no special prefix and should be parsed as a paragraph.

## Heading level 2

This is a second paragraph, separated by a blank line.
It exists to ensure multiple <p> elements are generated.

### Heading level 3

> This is a quote line
> that continues on the next line.
> And even a third line to ensure grouping works.

#### Heading level 4

- First bullet
- Second bullet with some _inline_ formatting
- Third bullet with **bold** text

##### Heading level 5

1. First item
2. Second item with **bold** text
3. Third item with _italic_ text

###### Heading level 6

####### (this line is just normal text, not a heading)

```
This is text that should remain
the same even with inline stuff
and code markers
```

"""


md1 = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    resulting_node = None
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        """
        print('BLOCK TYPE',block_type)
        print("*************************************")
        print(">>",block)
        print("*************************************")
        """
            
        
        
        
        match block_type:
            case BlockType.QUOTE:
                #print("QUOTE DETECTED")
                quote_lines = block.split('\n')
                processed_quote_lines = []
                for quote_line in quote_lines:
                    stripped = ''
                    quote_line = quote_line.lstrip()
                    if quote_line.startswith('> '):
                        stripped = quote_line[2:]
                    elif quote_line.startswith('>'):
                        stripped = quote_line[1:]
                    processed_quote_lines.append(stripped)
                quote_text = " ".join(processed_quote_lines)
                quote_children = text_to_children(quote_text)
                resulting_node = ParentNode("blockquote", quote_children)
                
            case BlockType.CODE:
                child_node = LeafNode('code',extract_code_text(block))
                resulting_node = ParentNode('pre',[child_node])
                
                
            case BlockType.HEADING:                
                [tag, value] = header_maker(block)                
                resulting_node = LeafNode(tag, value)                
                
            case BlockType.ORDERED_LIST:
                list_lines = block.split('\n')
                processed_list_lines = []
                for list_line in list_lines:
                    list_line = list_line[3:]
                    ordered_children = text_to_children(list_line)
                    processed_list_lines.append(ParentNode('li',ordered_children))
                
                resulting_node = ParentNode('ol',processed_list_lines)
                #print('ORDERED LIST >>>>',resulting_node)

                
                
            case BlockType.UNORDERED_LIST:
                #print("UNORDERED LIST SPOTTED")
                list_lines = block.split('\n')
                processed_list_lines = []
                for list_line in list_lines:
                    list_line = list_line[2:]
                    unordered_children = text_to_children(list_line)
                    processed_list_lines.append(ParentNode('li',unordered_children))
                
                resulting_node = ParentNode('ul',processed_list_lines)
                #print('UNORDERED NODE',resulting_node)
            case BlockType.PARAGRAPH:
                #1print("PARAGRAPH SPOTTED")
                #print(">>>",block)
                paragraph_text = block.replace("\n", " ")
                paragraph_children = text_to_children(paragraph_text)
                resulting_node = ParentNode("p", paragraph_children)
                
                
        children.append(resulting_node)
        resulting_node = None
    for child in children:
        pass
        #print('>>',child)
    #print("=======================================================================")
    #print(children)
    #print(len(children))
    #node = ParentNode("div", children)
    #print(node.to_html())
    return ParentNode("div", children)
        
        #print('>>>>',block_type,text_nodes)
        



def header_maker(block):
    splitted = block.split(' ',1)
    
    return f'h{len(splitted[0])}', splitted[1].strip()
    
          
def unordered_list_maker(block):
    pass
    

  # or wherever it is

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for tn in text_nodes:
        children.append(text_node_to_html_node(tn))
    return children
                
    
        



