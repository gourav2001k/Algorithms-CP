class Solution:
    def maxDiff(self, n: int) -> int:
        s = str(n)

        mx, a = '', ''
        for i in s:
            if not mx and i != '9':
                mx = i
            if mx and mx == i:
                a += '9'
            else:
                a += i

        if not int(s.replace(s[0], '0')):
            b = s.replace(s[0], '1')
            return int(a)-int(b)

        mn, b, t = '', '', ''
        for i in s:
            if i == '0':
                b += i
                continue
            if not mn and not b and i != '1':
                mn = i
                t = '1'
            if not mn and b and i != '1':
                mn = i
                t = '0'
            if mn and mn == i:
                b += t
            else:
                b += i

        return int(a)-int(b)
