# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/description/

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        n, P = len(power), 10**5+1
        power.sort()
        count = [0]
        mapp, idx = dict({0: 0}), 1
        revMap = dict({0: 0})
        for p in power:
            if p not in mapp:
                mapp[p] = idx
                revMap[idx] = p
                idx += 1
                count.append(0)
            count[mapp[p]] += 1

        out = [0]
        for i in range(1, idx):
            x = revMap[i]*count[i]
            if revMap[i-1]+2 < revMap[i]:
                x += out[i-1]
            elif i-2 >= 0 and revMap[i-2]+2 < revMap[i]:
                x += out[i-2]
            elif i-3 >= 0:
                x += out[i-3]
            x = max(x, out[i-1])
            if i-2 >= 0:
                x = max(x, out[-2])
            out.append(x)

        return out[-1]
