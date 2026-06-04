class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end


def main():
    trie = Trie()
    trie.insert("cat")
    trie.insert("car")
    print("yes" if trie.search("car") else "no", "yes" if trie.search("can") else "no")


if __name__ == "__main__":
    main()
