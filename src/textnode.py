from enum import Enum

class TextType(Enum):
#    NORMAL = ""
#    BOLD = ["<b>","</b>"]
#    ITALIC = ["<i>", "</i>"]
#    CODE = ["<code>", "</code>"]
#    LINKS = ["<a href=>", "</a>"]
#    IMAGES = ["<img src= alt=>"]

    NORMAL = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINKS = 5
    IMAGES = 6

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type.value
        self.url = url
        
    def __eq__(text_node_1, text_node_2):
        return text_node_1 == text_node_2

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"