# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        inDeg = Counter()
        g = defaultdict(list)
        for i in range(n):
            for ing in ingredients[i]:
                g[ing].append(recipes[i])
                inDeg[recipes[i]] += 1

        out = set()
        q = deque([])
        for sup in supplies:
            q.append(sup)

        while q:
            cur = q.pop()
            out.add(cur)
            for x in g[cur]:
                inDeg[x] -= 1
                if inDeg[x] == 0:
                    q.append(x)

        res = []
        for recipe in recipes:
            if recipe not in out:
                continue
            res.append(recipe)
        return res
