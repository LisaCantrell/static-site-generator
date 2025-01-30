from enum import Enum

class TextType(Enum):
    NORMAL = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINKS = 'links'
    IMAGES = 'images'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(first_node, second_node):
        is_equal = (
            first_node.text == second_node.text 
            and first_node.text_type == second_node.text_type
            and first_node.url == second_node.url)
        return is_equal
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        