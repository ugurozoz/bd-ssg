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
            html += f' {prop_key}="{self.props[prop_key]}"'
        return html
    
    
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    
        
    
    
    
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
            
        result =f'<{self.tag}{self.props_to_html()}>{inner_text}'
        for child in self.children:
            #print(child)
            result += child.to_html()
        result += f'</{self.tag}>'
        return result
        #print('-->',result)
 
 
 
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")
        
        
    