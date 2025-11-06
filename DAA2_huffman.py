class Node:
    def _init_(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_tree(text):
    freq = {ch: text.count(ch) for ch in set(text)}
    nodes = [Node(ch, f) for ch, f in freq.items()]

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        nodes.append(new_node)

    return nodes[0]

def make_codes(node, code="", codes=None):
    if codes is None:
        codes = {}
    if node.char is not None:     # leaf node
        codes[node.char] = code
    else:                         # internal node
        make_codes(node.left, code + "0", codes)
        make_codes(node.right, code + "1", codes)
    return codes

# main
text = input("Enter text: ")
root = build_tree(text)
codes = make_codes(root)

print("\nHuffman Codes:")
for ch, code in codes.items():
    print(ch, ":", code)