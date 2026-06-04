class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word):
        node = self
        for ch in word:
            node = node.children.setdefault(ch, Trie())
        node.end = True

    def _collect(self, prefix, out):
        if self.end:
            out.append(prefix)
        for ch in sorted(self.children):
            self.children[ch]._collect(prefix + ch, out)

    def autocomplete(self, prefix):
        node = self
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        out = []
        node._collect(prefix, out)
        return out


t = Trie()
for w in ("car", "card", "dog"):
    t.insert(w)
print(" ".join(t.autocomplete("car")))
