class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            ch = s[r]
            freq[ch] = freq.get(ch, 0) + 1
            
            while freq[ch] > 1:
                left_ch = s[l]
                freq[left_ch] -= 1
                l += 1
                
            curr_len = r - l + 1
            if curr_len > max_len:
                max_len = curr_len
                
        return max_len