class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
            
        p_count = {}
        window = {}
        for i in range(m):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            window[s[i]] = window.get(s[i], 0) + 1
            
        res = []
        if window == p_count:
            res.append(0)
            
        l = 0
        for r in range(m, n):
            right_ch = s[r]
            window[right_ch] = window.get(right_ch, 0) + 1
            
            left_ch = s[l]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]
            l += 1
            
            if window == p_count:
                res.append(l)
                
        return res