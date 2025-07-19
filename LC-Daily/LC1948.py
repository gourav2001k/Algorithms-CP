# https://leetcode.com/problems/delete-duplicate-folders-in-system/description/

class Node:
    def __init__(self, val):
        self.val = val
        self.child = dict()

    def getTotalPath(self):
        out = self.val
        for x in self.child:
            out += '{'+self.child[x].getTotalPath()+'}'
        return out

    def getKidsPath(self):
        return self.getTotalPath()[len(self.val):]


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        n = len(paths)
        paths.sort()
        root = Node('#root')

        def construct(path):
            cur = root
            for x in path:
                if x not in cur.child:
                    cur.child[x] = Node(x)
                cur = cur.child[x]

        for path in paths:
            construct(path)

        kids = set()
        toPrune = set()

        def dfs(root):
            kid = root.getKidsPath()
            if kid in kids:
                toPrune.add(kid)
                return
            if len(kid):
                kids.add(kid)
            for i in root.child:
                dfs(root.child[i])

        def dfsPrune(root):
            kid = root.getKidsPath()
            if kid in toPrune:
                return -1
            toDel = []
            for i in root.child:
                if dfsPrune(root.child[i]) == -1:
                    toDel.append(i)
            for i in toDel:
                del root.child[i]
            return 1

        dfs(root)
        dfsPrune(root)
        out = []

        def genPath(root, cur=[]):
            if len(cur):
                out.append(list(cur))
            for i in root.child:
                cur.append(root.child[i].val)
                genPath(root.child[i], cur)
                cur.pop()
        genPath(root)
        return out
