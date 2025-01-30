import unittest

from htmlnode import HTMLNode

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
        

    # def test_eq(self):
    # node = HTMLNode(tag="testtag", value="value", children="child", props="props")
    # node2 = HTMLNode(tag="testtag", value="value", children="child", props="props")
    # self.assertEqual(node, node2) 

if __name__ == "__main__":
    unittest.main()