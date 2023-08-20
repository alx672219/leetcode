class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Press backspace button at"#" and check whether backspaced values are the same.
        sl=[]
        tl=[]
        for i in s:
            if i=='#':
                sl=sl[:-1]
            else:
                sl.append(i)
        for i in t:
            if i=='#':
                tl=tl[:-1]
            else:
                tl.append(i)
        return sl == tl