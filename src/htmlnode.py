from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise  NotImplementedError("This method must be implemented in a subclass")
    
    def props_to_html(self):
        html = ''
        for prop_key in self.props.keys():
            html += f'{prop_key}="{self.props[prop_key]}" '
        return html
    
    
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self,tag,value,*args, **kwargs):
        super().__init__(tag,value,*args, **kwargs)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f'<{self.tag}>{self.value}</{self.tag}>'
    
    
        
    
    
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):        
        super().__init__(tag=tag, value=None, children=children, props=props)
        #print('>>',children)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError('Missing tag value')
        if self.children == None or self.children == {}:
            raise ValueError('Children dont exist')
        inner_text = self.value if self.value != None else '' 
            
        result =f'<{self.tag}>{inner_text}'
        for child in self.children:
            #print(child)
            result += child.to_html()
        result += f'</{self.tag}>'
        return result
        #print('-->',result)
 
 
 
def text_node_to_html_node(text_node: TextNode):
    match(text_node.text_type):
        case TextType.TEXT:
            return LeafNode(text_node.text)
        case TextType.BOLD:
            return LeafNode(text_node.text, "b")
        case TextType.ITALIC:
            return LeafNode(text_node.text, "i")
        case TextType.CODE:
            return LeafNode(text_node.text, "code")
        case TextType.LINK:
            return ParentNode("a", [LeafNode(text_node.text)], {"href": text_node.url})
        case TextType.IMAGE:
            return ParentNode("img", [], {"src": text_node.url, "alt": text_node.text})

     
        
        
    