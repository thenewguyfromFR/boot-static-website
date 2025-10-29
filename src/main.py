from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    textnode = TextNode("test of the TextNode creation", TextType.BOLD, "https://www.lemonde.fr/")
    print(textnode)

    htmlnode = HTMLNode("a", "this is an HTMLNode", [1, 2, 3], {"href": "https://www.google.com", "target": "_blank",})
    print(htmlnode)

    htmlnode = HTMLNode("a", "this is an HTMLNode", [1, 2, 3])
    print(htmlnode)

main()