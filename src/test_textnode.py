import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is not a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_texttype(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_url_to_None(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.lemonde.fr/")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_None_to_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "http://www.lemonde.fr/")
        self.assertNotEqual(node, node2)

    def test_not_eq_diff_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.lemonde.fr/")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://www.laposte.fr/")
        self.assertNotEqual(node, node2)

    def test_str_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.lemonde.fr/")
        node_descr = str(node)
        self.assertEqual(node_descr, "TextNode(This is a text node, bold text, http://www.lemonde.fr/)")

    def test_str_with_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node_descr = str(node)
        self.assertEqual(node_descr, "TextNode(This is a text node, bold text, None)")

    def test_texttype_plain(self):
        node = TextNode("This is a plain text node", TextType.TEXT)
        node_descr = str(node)
        self.assertEqual(node_descr, "TextNode(This is a plain text node, plain text, None)")

    def test_texttype_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node_descr = str(node)
        self.assertEqual(node_descr, "TextNode(This is a bold text node, bold text, None)")

    def test_texttype_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        node_descr = str(node)
        self.assertEqual(node_descr, "TextNode(This is an italic text node, italic text, None)")

    def test_texttype_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        node_descr = str(node)
        self.assertEqual(node_descr, "TextNode(This is a code text node, code text, None)")

    def test_texttype_link(self):
        node = TextNode("This is a link text node", TextType.LINK)
        node_descr = str(node)
        self.assertEqual(node_descr, "TextNode(This is a link text node, link, None)")

    def test_texttype_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE)
        node_descr = str(node)
        self.assertEqual(node_descr, "TextNode(This is an image text node, image, None)")


if __name__ == "__main__":
    unittest.main()

