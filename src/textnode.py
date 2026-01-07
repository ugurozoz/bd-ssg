from enum import Enum


class TextNode:
    def __init__(self,text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self,node1):
        return self.text == node1.text and self.text_type == node1.text_type and self.url == node1.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
   
   
    

class TextType(Enum):
    ITALIC = 'italic'
    BOLD = 'bold'
    TEXT = 'text'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'
 
 
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

