import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # for heapq comparisons
    def __lt__(self, other):
        return self.freq < other.freq

def build_tree(text):
    text = text.replace(" ", "")
    freq = Counter(text)

    print("\nCharacter Frequencies (excluding spaces):")
    for ch, fr in freq.items():
        print(f"{repr(ch)} : {fr} times")

    heap = [Node(ch, fr) for ch, fr in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)

    return heap[0], freq

def make_codes(node, code="", codes=None):
    if codes is None:
        codes = {}
    if node.char is not None:
        codes[node.char] = code
    else:
        make_codes(node.left, code + "0", codes)
        make_codes(node.right, code + "1", codes)
    return codes

def encode(text, codes):
    return "".join(codes[ch] for ch in text.replace(" ", ""))

def decode(encoded, root):
    decoded = ""
    curr = root
    for bit in encoded:
        curr = curr.left if bit == "0" else curr.right
        if curr.left is None and curr.right is None:
            decoded += curr.char
            curr = root
    return decoded

# ---------------- MAIN ----------------
text = input("Enter text: ")

root, freq = build_tree(text)
codes = make_codes(root)

print("\nHuffman Codes:")
for ch, code in codes.items():
    print(f"{repr(ch)} : {code}")

encoded = encode(text, codes)
print("\nEncoded String:")
print(encoded)

print("\nGrouped by 8 bits:")
for i in range(0, len(encoded), 8):
    print(encoded[i:i+8], end=" ")
print("\n")

decoded = decode(encoded, root)
print("Decoded String (no spaces):")
print(decoded)
