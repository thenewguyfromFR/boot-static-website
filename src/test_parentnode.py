import unittest

from htmlnode import ParentNode, LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_with_one_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        with self.assertRaises(ValueError): ParentNode(None, [child_node]).to_html()

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError): ParentNode("p", None).to_html()

    def test_to_html_empty_children(self):
        with self.assertRaises(ValueError): ParentNode("p", []).to_html()


if __name__ == "__main__":
    unittest.main()

