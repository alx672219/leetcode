class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        count = 0
        ans = ['']
        for i in reversed(range(n)): # 뒤로 하는 이유는 맨 처음 그룹이 can be shorter than k
            if (s[i] != '-'):
                ans += s[i].upper()
                count = count + 1
                if (count == k):
                    count = 0
                    ans += '-'
     
        # Make sure the output doesn't start with a dash
        if (len(ans) > 0 and ans[len(ans)-1] == '-'):
            ans = ans[:-1] # 만약에 첫번째(마지막)가 - 면 첫번째(마지막) 삭제
        ans = ans[::-1] # 다시 reverse
        result = "".join(ans)
        return result