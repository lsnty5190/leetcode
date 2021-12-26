from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
        
        minlen = 201
        for s in strs:
            if len(s) < minlen: minlen = len(s)
                
        index = 0
        i = 0
        
        while i < minlen:
            
            rep = set()
            rep.add(strs[0][i])
            repflag = False
            
            for s in strs:
                if s[i] not in rep:
                    index = i
                    repflag = True
                    break
            if repflag: break
            i += 1
        
        if index == 0: return ""
        else: return strs[0][:index]

strs = ["flower","flow","flight"]
out = longestCommonPrefix(strs)
print(out)