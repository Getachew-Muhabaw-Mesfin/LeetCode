class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
        return Counter(s)==Counter(t)
        if len(s)!=len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
            # countS[s[i]]=s.count(s[i])
            # countT[t[i]]=t.count(t[i])

        for c in countS:
            if countS[c]!=countT.get(c,0):
                return False
        return True


        
        