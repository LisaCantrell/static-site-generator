import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, url="www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, url="www.test.com")
        self.assertEqual(node, node2)

    def test_url_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD, url="www.sample.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, url="www.test.com")
        self.assertNotEqual(node, node2)

    def test_content_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_text_text_to_html_vs_leafnode(self):
        text_node = TextNode("testing plain text", TextType.TEXT)
        converted_to_html = text_node.text_node_to_html_node()
        html_node = LeafNode(None, "testing plain text", None)
        self.assertEqual(
            converted_to_html.tag, html_node.tag
        )
        self.assertEqual(
            converted_to_html.value, html_node.value
        )
        self.assertEqual(
            converted_to_html.children, html_node.children
        )
        self.assertEqual(
            converted_to_html.props, html_node.props
        )

    def test_bold_text_to_html_vs_leafnode(self):
        text_node = TextNode("testing bold text", TextType.BOLD)
        converted_to_html = text_node.text_node_to_html_node()
        html_node = LeafNode("b", "testing bold text", None)
        self.assertEqual(
            converted_to_html.tag, html_node.tag
        )
        self.assertEqual(
            converted_to_html.value, html_node.value
        )
        self.assertEqual(
            converted_to_html.children, html_node.children
        )
        self.assertEqual(
            converted_to_html.props, html_node.props
        )

    def test_link_text_to_html_vs_leafnode(self):
        text_node = TextNode("testing link text", TextType.LINK, "https://www.test.dev")
        converted_to_html = text_node.text_node_to_html_node()
        html_node = LeafNode("a", "testing link text", {"href": "https://www.test.dev"})
        self.assertEqual(
            converted_to_html.tag, html_node.tag
        )
        self.assertEqual(
            converted_to_html.value, html_node.value
        )
        self.assertEqual(
            converted_to_html.children, html_node.children
        )
        self.assertEqual(
            converted_to_html.props, html_node.props
        )

    def test_image_text_to_html_vs_leafnode(self):
        text_node = TextNode("testing image text", TextType.IMAGE, "https://www.test.dev")
        converted_to_html = text_node.text_node_to_html_node()
        html_node = LeafNode("img", "", {"src": "https://www.test.dev", "alt": "testing image text"})
        self.assertEqual(
            converted_to_html.tag, html_node.tag
        )
        self.assertEqual(
            converted_to_html.value, html_node.value
        )
        self.assertEqual(
            converted_to_html.children, html_node.children
        )
        self.assertEqual(
            converted_to_html.props, html_node.props
        )


if __name__ == "__main__":
    unittest.main()