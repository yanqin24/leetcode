class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        fastmove=0
        cur_end=0
        jump=0
        for i in range(n-1):
            fastmove=max(fastmove,i+nums[i])
            if cur_end==i:
                jump+=1
                cur_end=fastmove
        return jump


