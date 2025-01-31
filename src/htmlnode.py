

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Must have a value")
        if self.tag is None:
            return self.value
        property_string = self.props_to_html()
        html_string = f'<{self.tag}{property_string}>{self.value}</{self.tag}>'
        return html_string
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Must have a tag")
        if self.children is None:
            raise ValueError("Parent nodes must have children")
        child_html_string = ''
        for child in self.children:
            if isinstance(child, ParentNode):
                child_html_string += child.to_html()
            else:
                property_string = child.props_to_html()
                if child.tag is None:
                    child_html_string += child.value
                else:
                    child_html_string += f'<{child.tag}{property_string}>{child.value}</{child.tag}>'
        parent_prop_string = self.props_to_html()
        html_string = f'<{self.tag}{parent_prop_string}>{child_html_string}</{self.tag}>'
        return html_string
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
