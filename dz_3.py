class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, a: str) -> None:
        cur = self.root
        for x in a:
            if x not in cur.children:
                cur.children[x] = TrieNode()
            cur = cur.children[x]
        cur.isEnd = True

    def search(self, a: str) -> bool:

        def find(cur, i=0):
            if i == len(a):
                return cur.isEnd

            if a[i] == '.':
                return any(find(x, i + 1) for x in cur.children.values())

            if a[i] in cur.children:
                return find(cur.children[a[i]], i + 1)

            return False

        return find(self.root)