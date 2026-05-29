# https://leetcode.com/problems/longest-common-suffix-queries/description

class Trie:
    def __init__(self):
        self.nodes = [None for i in range(26)]
        self.indexs = []

    def find(self, x):
        return self.nodes[ord(x)-97]

    def addIdx(self, x):
        self.indexs.append(x)

    def put(self, x, node):
        self.nodes[ord(x)-97] = node

    def __str__(self):
        return self.nodes.__str__()


class Solution:
    def stringIndices(self, words: List[str], queries: List[str]) -> List[int]:
        n = len(words)
        for i in range(n):
            words[i] = words[i][::-1]

        root = Trie()
        words = list(sorted(enumerate(words), key=lambda x: len(x[1])))

        for idx, word in words:
            root.addIdx(idx)
            cur = root
            for x in word:
                nxt = cur.find(x)
                if not nxt:
                    nxt = Trie()
                nxt.addIdx(idx)
                cur.put(x, nxt)
                cur = nxt

        out = []
        for q in queries:
            cur = root
            for x in q[::-1]:
                if cur.find(x):
                    cur = cur.find(x)
                else:
                    break
            out.append(cur.indexs[0])
        return out
