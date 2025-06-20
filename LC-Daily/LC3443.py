# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/description

class Solution:
    def maxDistance(self, dirs: str, k: int) -> int:
        l = len(dirs)
        n, s, e, w = 0, 0, 0, 0
        out = 0
        for i in range(l):
            kk = k
            if dirs[i] == "N":
                n += 1
            elif dirs[i] == "S":
                s += 1
            elif dirs[i] == "E":
                e += 1
            else:
                w += 1
            t = max(n, s)
            if min(n, s) <= kk:
                t += min(n, s)
                kk -= min(n, s)
            else:
                t -= min(n, s)-kk
                t += kk
                kk = 0
            t += max(w, e)
            if min(w, e) <= kk:
                t += min(w, e)
                kk -= min(w, e)
            else:
                t -= min(w, e)-kk
                t += kk
                kk = 0
            out = max(out, t)
        return out
