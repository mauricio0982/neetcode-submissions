from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     n=len(s)
     m=len(t)
     ca=Counter()
     cb=Counter()
     
     if n!=m:
         return False


     for i in s:
        if i not in ca:
            ca[i]=1
        else:
            ca[i]+=1

     for i in t:
        if i not in cb:
            cb[i]=1
        else:
            cb[i]+=1 
     return ca==cb