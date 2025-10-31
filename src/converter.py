from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
import re

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
            html_node = LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            html_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception(f"Invalid Text Type: {text_node.text_type}")

    return html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            node_text = node.text
            if node_text.count(delimiter) % 2 != 0:
                raise Exception(f"Invalid Markdown syntax: missing closing character '{delimiter}'")
            
            open_del = node_text.startswith(delimiter)
            split_text = node.text.split(delimiter)
            
            for i in range(1 if open_del else 0, len(split_text)):
                if open_del:
                    new_text_type = text_type
                    open_del = False
                else:
                    new_text_type = TextType.TEXT
                    open_del = True
                if len(split_text[i]) > 0:
                    new_nodes.append(TextNode(split_text[i], new_text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    #"This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    #"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    return re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    pass
