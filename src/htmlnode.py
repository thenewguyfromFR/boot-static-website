class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = "None"
        if self.props is not None and len(self.props) > 0:
            result = ""
            for key, value in self.props.items():
                result += f' {key}="{value}"'
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == "" or self.value is None:
            raise ValueError
        
        match self.tag:
            case "h1" | "h2" | "h3" | "h4" | "h5" | "h6" | "p" | "b" | "i" | "li" | "blockquote" | "code":
                return f'<{self.tag}>{str(self.value)}</{self.tag}>'
            case "a":
                return f'<a{self.props_to_html()}>{self.value}</a>'
            case "img":
                return f'<img{self.props_to_html()} alt="{self.value}" />'
            case _:
                return str(self.value)
        