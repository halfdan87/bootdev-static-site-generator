import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    #    def test_eq(self):
    #        node = HTMLNode("div", "Test", [], {})
    #        node2 = HTMLNode("div", "Test", [], {})
    #        self.assertEqual(node, node2)
    #
    #    def test_eq_children(self):
    #        child = HTMLNode("p", "TestChild", [], {})
    #        node = HTMLNode("div", "Test", [child], {"test": "test"})
    #        child2 = HTMLNode("p", "TestChild", [], {})
    #        node2 = HTMLNode("div", "Test", [child2], {"test": "test"})
    #        self.assertEqual(node, node2)
    def test_props_to_html(self):
        node = HTMLNode("div", "Test", [], {"test": "testVal", "other": "otherVal"})
        self.assertEqual('test="testVal" other="otherVal"', node.props_to_html())

    def test_leaf_to_html(self):
        node = LeafNode("Test", "div", {"test": "testVal", "other": "otherVal"})
        self.assertEqual('<div test="testVal" other="otherVal">Test</div>', node.to_html())

    def test_parent_to_html(self):
        node = ParentNode(
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
            "p",
        )

        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())


if __name__ == "__main__":
    unittest.main()
