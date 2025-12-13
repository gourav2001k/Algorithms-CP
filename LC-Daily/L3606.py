# https://leetcode.com/problems/coupon-code-validator/description/

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)

        def validate(coupon):
            if not coupon:
                return False
            for x in coupon:
                if not x.isalnum() and x != "_":
                    return False
            return True

        valid = defaultdict(list)
        bb = ["electronics", "grocery", "pharmacy", "restaurant"]
        for i in range(n):
            c = code[i]
            if businessLine[i] not in bb:
                continue
            if not isActive[i]:
                continue
            if not validate(c):
                continue
            valid[businessLine[i]].append(c)

        for business in valid:
            valid[business].sort()

        out = []
        for business in bb:
            out += valid[business]
        return out
