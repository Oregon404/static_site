import textnode

print("hello world")

def main():
    tnode = textnode.TextNode("This is a text node", textnode.TextType.BOLD, "https://www.boot.dev")
    print(tnode)
main()