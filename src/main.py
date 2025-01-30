# import textnode
from textnode import TextNode, TextType

def main():
    test_text_node = TextNode("sampletext", TextType.BOLD, "https://www.dummysite.com")
    print(test_text_node)
main()