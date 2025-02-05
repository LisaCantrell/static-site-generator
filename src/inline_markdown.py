import re
from textnode import TextType, TextNode

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Missing a delimiter")
        
        fragment_list = node.text.split(delimiter)

        for i in range(len(fragment_list)):
            if i % 2 != 0:
                new_nodes.append(TextNode(fragment_list[i], text_type))
            else:
                if fragment_list[i] == "":
                    continue
                new_nodes.append(TextNode(fragment_list[i], TextType.TEXT))

    return new_nodes 

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        current_text = node.text
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            return [node]
        
        fragments = []

        while len(links) >= 0:
            if len(links) == 0:
                if len(current_text) == 0:
                    break
                else:
                    fragments.append((current_text, TextType.TEXT))
                    break
            current_link = links[0]
            split_text = current_text.split(f"[{current_link[0]}]({current_link[1]})")
            if split_text[0] != "":
                fragments.append((split_text[0], TextType.TEXT))
            fragments.append((current_link[0], TextType.LINK, current_link[1]))
            current_text = split_text[-1]
            links.pop(0)

        new_nodes = []
        for fragment in fragments:
            if fragment[1] == TextType.LINK:
                new_nodes.append(TextNode(fragment[0], TextType.LINK, fragment[2]))
            else:
                new_nodes.append(TextNode(fragment[0], TextType.TEXT))

        return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        current_text = node.text
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            return [node]
        
        fragments = []

        while len(images) >= 0:
            if len(images) == 0:
                if len(current_text) == 0:
                    break
                else:
                    fragments.append((current_text, TextType.TEXT))
                    break
            current_image = images[0]
            split_text = current_text.split(f"![{current_image[0]}]({current_image[1]})")
            if split_text[0] != "":
                fragments.append((split_text[0], TextType.TEXT))
            fragments.append((current_image[0], TextType.IMAGE, current_image[1]))
            current_text = split_text[-1]
            images.pop(0)

        new_nodes = []
        for fragment in fragments:
            if fragment[1] == TextType.IMAGE:
                new_nodes.append(TextNode(fragment[0], TextType.IMAGE, fragment[2]))
            else:
                new_nodes.append(TextNode(fragment[0], TextType.TEXT))

        return new_nodes

node = TextNode(
    "![image](https://www.example.COM/IMAGE.PNG)",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])
print(new_nodes)