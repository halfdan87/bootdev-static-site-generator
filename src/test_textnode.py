import unittest

from src.textnode import extract_markdown_images, extract_markdown_links
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_extract_markdown_images(self):
        test_text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        result = extract_markdown_images(test_text)
        self.assertEqual(result[0][0], "image")
        self.assertEqual(
            result[0][1],
            "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
        )
        self.assertEqual(result[1][0], "another")
        self.assertEqual(
            result[1][1],
            "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png",
        )

    def test_extract_markdown_links(self):
        test_text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        result = extract_markdown_links(test_text)
        self.assertEqual(result[0][0], "link")
        self.assertEqual(result[0][1], "https://www.example.com")
        self.assertEqual(result[1][0], "another")
        self.assertEqual(result[1][1], "https://www.example.com/another")


if __name__ == "__main__":
    unittest.main()
