import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://test.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://test.dev"',
        )

    def test_repr(self):
        props_dict = {
            "href": "https://www.google.com",
            "target": "_blank"}

        node = HTMLNode(tag="<a>", value="value", children="child",props=props_dict)
        self.assertEqual("HTMLNode(<a>, value, child, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node))
        
    def test_eq(self):
        node = HTMLNode(
            "div",
            "Some text here",
        )
        self.assertEqual(
            node.tag,
            "div"
        )
        self.assertEqual(
            node.value,
            "Some text here",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
        
class TestLeafNode(unittest.TestCase):
    def test_with_props(self):
        props_dict = {
            "href": "https://www.google.com"
            }

        node = LeafNode("a", "some test text", props_dict)
        self.assertEqual('<a href="https://www.google.com">some test text</a>', node.to_html())

    def test_value_exception(self):
        props_dict = {
            "href": "https://www.google.com"
            }
        node = LeafNode("a", None, props_dict)
        with self.assertRaises(Exception) as context:
            node.to_html()

            self.assertTrue('Must hava a value' in str(context.exception))
    
    def test_eq(self):
        props_dict = {
            "href": "https://www.google.com"
            }

        node = LeafNode("a", "some test text", props_dict)
        self.assertEqual(
            node.tag,
            "a"
        )
        self.assertEqual(
            node.value,
            "some test text",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            props_dict,
        )

if __name__ == "__main__":
    unittest.main()