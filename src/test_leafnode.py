import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_h2(self):
        node = LeafNode("h2", "Hello, world!")
        self.assertEqual(node.to_html(), "<h2>Hello, world!</h2>")

    def test_leaf_to_html_h3(self):
        node = LeafNode("h3", "Hello, world!")
        self.assertEqual(node.to_html(), "<h3>Hello, world!</h3>")

    def test_leaf_to_html_h4(self):
        node = LeafNode("h4", "Hello, world!")
        self.assertEqual(node.to_html(), "<h4>Hello, world!</h4>")

    def test_leaf_to_html_h5(self):
        node = LeafNode("h5", "Hello, world!")
        self.assertEqual(node.to_html(), "<h5>Hello, world!</h5>")

    def test_leaf_to_html_h6(self):
        node = LeafNode("h6", "Hello, world!")
        self.assertEqual(node.to_html(), "<h6>Hello, world!</h6>")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")

    def test_leaf_to_html_li(self):
        node = LeafNode("li", "Hello, world!")
        self.assertEqual(node.to_html(), "<li>Hello, world!</li>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Hello, world!", {"href":"https://www.lemonde.fr"})
        self.assertEqual(node.to_html(), '<a href="https://www.lemonde.fr">Hello, world!</a>')

    def test_leaf_to_html_img(self):
        node = LeafNode("img", "", {"src":"https://www.lemonde.fr", "alt":"Hello, world!"})
        self.assertEqual(node.to_html(), '<img src="https://www.lemonde.fr" alt="Hello, world!"/>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!", {"src":"https://www.lemonde.fr"})
        self.assertEqual(node.to_html(), 'Hello, world!')

    def test_leaf_to_html_unknown_tag(self):
        node = LeafNode("c", "Hello, world!", {"src":"https://www.lemonde.fr"})
        self.assertEqual(node.to_html(), '<c src="https://www.lemonde.fr">Hello, world!</c>')

    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError): LeafNode("p", None, {"src":"https://www.lemonde.fr"}).to_html()


if __name__ == "__main__":
    unittest.main()

