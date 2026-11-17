class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        max_freq = 0
        max_len = 0
        
        for r in range(len(s)):
            ch = s[r]
            freq[ch] = freq.get(ch, 0) + 1
            if freq[ch] > max_freq:
                max_freq = freq[ch]
                
            while (r - l + 1) - max_freq > k:
                left_ch = s[l]
                freq[left_ch] -= 1
                l += 1
                
            curr_len = r - l + 1
            if curr_len > max_len:
                max_len = curr_len
                
        return max_len