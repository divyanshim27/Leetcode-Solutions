class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        doubled = s + s
        n = len(doubled)
        m = len(goal)
        
        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if doubled[i + j] != goal[j]:
                    match = False
                    break
            if match:
                return True
                
        return False