from textnode import TextNode, TextType

def main():
    textnode = TextNode("test of the TextNode creation", TextType.bold_text, "https://www.lemonde.fr/")
    print(textnode)

main()