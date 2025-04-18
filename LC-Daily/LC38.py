# https://leetcode.com/problems/count-and-say/description/
class Solution:
    def countAndSay(self, n: int) -> str:
        n -= 1
        seq = ['1']
        while n:
            n -= 1
            nSeq = []
            c, i = 1, 1
            while i < len(seq):
                if seq[i] == seq[i-1]:
                    c += 1
                else:
                    nSeq.append(str(c))
                    nSeq.append(seq[i-1])
                    c = 1
                i += 1
            nSeq.append(str(c))
            nSeq.append(seq[len(seq)-1])
            seq = nSeq

        return "".join(seq)
