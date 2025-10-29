from textnode import TextNode, TextType

def main():
    textnode = TextNode("test of the TextNode creation", TextType.BOLD, "https://www.lemonde.fr/")
    print(textnode)

main()