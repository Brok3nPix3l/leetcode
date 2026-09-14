class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        pre, suf = p.split('*')

        if pre == '':
            return suf in s
        elif suf == '':
            return pre in s
        else:
            pi, si = s.find(pre), s.rfind(suf)
            return pi != -1 and pi + len(pre) <= si