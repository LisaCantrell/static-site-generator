import unittest

from textnode import TextNode, TextType
from markdownhandling import split_nodes_delimiter

class Test_MarkdownHandling(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
                        ]
                    )
    
    def test_noteq(self):
        node = TextNode("This is text with a different `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertNotEqual(
            new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
                        ]
                    )
    
    def test_not_text(self):
        node = TextNode("This is text with a different `code block` word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(node, new_nodes[0])

    def test_eq_mult_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is `more code` block", TextType.TEXT)
        node3 = TextNode("look here is `even more code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2, node3], "`", TextType.CODE)
        self.assertEqual(
            new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is ", TextType.TEXT),
            TextNode("more code", TextType.CODE),
            TextNode(" block", TextType.TEXT),
            TextNode("look here is ", TextType.TEXT),
            TextNode("even more code", TextType.CODE),
                        ]
                    )