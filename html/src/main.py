# to run: python3 -m http.server 8888

# cheat sheet: https://www.boot.dev/lessons/220f456c-ad0b-4455-a236-31f4ebab3bc5

from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)


main()