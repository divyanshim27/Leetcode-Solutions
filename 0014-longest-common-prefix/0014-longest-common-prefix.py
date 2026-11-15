class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        shortest = strs[0]
        for s in strs:
            if len(s) < len(shortest):
                shortest = s
                
        n = len(shortest)
        for i in range(n):
            char = shortest[i]
            for s in strs:
                if s[i] != char:
                    return shortest[:i]
                    
        return shortest