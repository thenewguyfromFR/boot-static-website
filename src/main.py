from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from converter import text_node_to_html_node

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

if __name__ == "__main__":
    main()