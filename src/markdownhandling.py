from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Missing a closing delimiter")
        
        fragment_list = node.text.split(delimiter)

        for i in range(len(fragment_list)):
            if i % 2 != 0:
                new_nodes.append(TextNode(fragment_list[i], text_type))
            else:
                if fragment_list[i] == "":
                    continue
                new_nodes.append(TextNode(fragment_list[i], TextType.TEXT))

    return new_nodes 



