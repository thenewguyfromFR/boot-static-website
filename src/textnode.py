from enum import Enum

class TextType(Enum):
    plain_text = "plain text"
    bold_text = "bold text"
    italic_text = "italic text"
    code_text = "code text"
    link = "link"
    image = "image"


class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eg__(self, other):
        return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

    
