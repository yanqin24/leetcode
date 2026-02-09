class Solution:
    def canJump(self, nums):
        farthest = 0
        for i, step in enumerate(nums):
            if farthest < i:
                return False
            farthest = max(farthest, i + step)
        return True
