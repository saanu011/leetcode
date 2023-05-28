class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        ls1 = [0]*127
        ls2 = [0]*127
        for i in range(len(s1)):
            ls1[ord(s1[i])] += 1
            ls2[ord(s2[i])] += 1
        
        if ls1 == ls2:
            return True
        for i in range(len(s1), len(s2)):
            ls2[ord(s2[i])] += 1
            ls2[ord(s2[i-len(s1)])] -= 1
            if ls1 == ls2:
                return True
        return False
