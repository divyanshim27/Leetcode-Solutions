class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        built = ""
        for w in words:
            built += w
            if built == s:
                return True
            if len(built) > len(s):
                return False
        return False