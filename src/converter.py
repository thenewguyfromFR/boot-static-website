from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            html_node = LeafNode(None, text_node.text)
        case TextType.BOLD:
            html_node = LeafNode("b", text_node.text)
        case TextType.ITALIC:
            html_node = LeafNode("i", text_node.text)
        case TextType.CODE:
            html_node = LeafNode("code", text_node.text)
        case TextType.LINK:
            html_node = LeafNode("a", text_node.text, {"href":f"{text_node.url}"})
        case TextType.IMAGE:
            html_node = LeafNode("img", text_node.text, {"src":f"{text_node.url}"})
        case _:
            raise Exception("Unknown Text Type")

    return html_node

