import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_empty(self):
        node = HTMLNode()
        node_descr = str(node)
        self.assertEqual(node_descr, "HTMLNode(None, None, None, )")

    def test_tag(self):
        node = HTMLNode("a")
        node_descr = str(node)
        self.assertEqual(node_descr, "HTMLNode(a, None, None, )")

    def test_value(self):
        node = HTMLNode(None, "This is a HTMLNode")
        node_descr = str(node)
        self.assertEqual(node_descr, "HTMLNode(None, This is a HTMLNode, None, )")

    def test_children(self):
        node = HTMLNode(None, None, [1, 2, 3])
        node_descr = str(node)
        self.assertEqual(node_descr, "HTMLNode(None, None, [1, 2, 3], )")

    def test_props(self):
        node = HTMLNode(None, None, None, {"href":"https://www.lemonde.fr", "target": "/img/lemonde.jpg"})
        node_descr = str(node)
        self.assertEqual(node_descr, 'HTMLNode(None, None, None,  href="https://www.lemonde.fr" target="/img/lemonde.jpg")')


if __name__ == "__main__":
    unittest.main()

