from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    textnode = TextNode("test of the TextNode creation", TextType.BOLD, "https://www.lemonde.fr/")
    print(textnode)

    htmlnode = HTMLNode("a", "this is an HTMLNode", [1, 2, 3], {"href": "https://www.google.com", "target": "_blank",})
    print(htmlnode)

    htmlnode = HTMLNode("a", "this is an HTMLNode", [1, 2, 3])
    print(htmlnode)

    leafnode = LeafNode("p", "Hello, world!")
    print(leafnode.to_html())

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(node.to_html())

    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    print(html_node.to_html())

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            html_node = LeafNode(None, text_node.text)
        case TextType.BOLD:
            html_tag = LeafNode("b", text_node.text)
        case TextType.ITALIC:
            html_tag = LeafNode("i", text_node.text)
        case TextType.CODE:
            html_tag = LeafNode("code", text_node.text)
        case TextType.LINK:
            html_tag = LeafNode("link", text_node.text, {"href":f"{text_node.url}"})
        case TextType.IMAGE:
            html_tag = LeafNode("img", text_node.text, {"src":f"{text_node.url}"})
        case _:
            raise Exception("Unknown Text Type")

    return html_node

main()