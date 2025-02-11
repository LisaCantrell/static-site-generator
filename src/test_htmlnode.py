import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_value_exception(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, "Normal text")
        child3 = LeafNode("i", "italic text")
        child4 = LeafNode(None, "Normal text")
        child_list =  [
                child1,
                child2,
                child3,
                child4,
            ]
        node = ParentNode(
            "p", child_list)
        self.assertEqual(
            node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_no_children(self):
        node = ParentNode("p", [])
            
        with self.assertRaises(Exception) as context:
            node.to_html()

            self.assertTrue('Parent nodes must have children' in str(context.exception))
    
    def test_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
            
        with self.assertRaises(Exception) as context:
            node.to_html()

            self.assertTrue('Must have a tag' in str(context.exception))

    def test_repr(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
            ],
        )
        self.assertEqual("ParentNode(p, [LeafNode(b, Bold text, None)], None)", repr(node))



    def test_nested_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p", [LeafNode("b", "Bold text")])
            ],
        )
        self.assertEqual(
            node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b></p></p>"
        )


if __name__ == "__main__":
    unittest.main()