import unittest

from textnode import TextNode, TextType
from htmlnode import ParentNode, LeafNode
from converter import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>This is a italic node</i>")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.lemonde.fr")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.lemonde.fr">This is a link node</a>')

    def test_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, "https://www.lemonde.fr")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.lemonde.fr" alt="This is a image node" />')

    def test_unknown_tag(self):
        node = TextNode("This is a unknown node", "unknown", "https://www.lemonde.fr")
        with self.assertRaises(Exception): text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()

