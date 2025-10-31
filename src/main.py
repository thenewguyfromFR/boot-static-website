from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from converter import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links

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

    node1 = TextNode("This is a text node with `code part` included", TextType.TEXT)
    node2 = TextNode("`code part at the beginning` added", TextType.TEXT)
    node3 = TextNode("and with `code part at the end`", TextType.TEXT)
    print(split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE))

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))

if __name__ == "__main__":
    main()