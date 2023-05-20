class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ""
        arr = [0]*128
        big = 0
        l = len(s)
        i, j = 0, 0
    
        cur = 0
        while i < l and j<l:
            ind = ord(s[j])
            if arr[ind] == 0:
                arr[ind] += 1
                cur += 1
                j+=1
            else:
                arr[ord(s[i])] -= 1
                i += 1
                cur -= 1

            if cur>big:
                big = cur
        return big