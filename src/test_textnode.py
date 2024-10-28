import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a poop node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_hyperlink(self):
        node = TextNode("This is a text node with link", TextType.ITALIC,"https://www.boot.dev/")
        node2 = TextNode("This is a text node with link", TextType.ITALIC,"https://www.boot.dev/")
        self.assertEqual(node, node2)
    
    def test_code(self):
        node = TextNode("Hello, world!", TextType.CODE)
        node2 = TextNode("Hello, world!", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()