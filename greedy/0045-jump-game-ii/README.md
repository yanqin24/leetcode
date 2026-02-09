# 45. Jump Game II

**Topic:** Greedy (Range Expansion)  
**Difficulty:** Medium  
**Link:** LeetCode 45

## Problem
Given an integer array `nums`, you are initially positioned at index `0`.  
Each element `nums[i]` represents your maximum jump length from that position.  
Return the minimum number of jumps to reach the last index.

## Intuition (Greedy)
This is like scanning level by level (BFS over ranges), but in `O(n)`:
- `farthest`: the farthest index we can reach while scanning the current range.
- `cur_end`: the end boundary of the current jump range.
- `jumps`: number of jumps taken so far.

As we scan indices, we keep expanding `farthest`.
When `i == cur_end`, we have finished the current range, so we must take one jump:
- `jumps += 1`
- `cur_end = farthest`

This ensures each jump extends to the maximum reachable boundary, yielding the minimum jumps.

## Algorithm
1. Initialize `jumps = 0`, `cur_end = 0`, `farthest = 0`.
2. Iterate `i` from `0` to `n-2` (no need to jump from the last index):
   - Update `farthest = max(farthest, i + nums[i])`
   - If `i == cur_end`:
     - `jumps += 1`
     - `cur_end = farthest`
3. Return `jumps`

## Complexity
- **Time:** `O(n)`
- **Space:** `O(1)`

## Notes
- Iterate only to `n-2` to avoid counting an extra jump at the end.
- This greedy is equivalent to choosing the next jump that covers the largest possible range.
