class Solution:
  def toLowerCase(self, s: str) -> str:
    res = []
    for ch in s:
      code = ord(ch)
      if 65 <= code <= 90:
        res.append(chr(code + 32))
      else:
        res.append(ch)
    return "".join(res)