# 55. Jump Game

**Topic:** Greedy  
**Difficulty:** Medium  
**Link:** LeetCode 55

## Problem
Given an integer array `nums`, you are initially positioned at index `0`.  
Each element `nums[i]` represents your maximum jump length from that position.  
Return `true` if you can reach the last index, otherwise return `false`.

## Intuition (Greedy)
Maintain `farthest`, the farthest index reachable so far.
- At index `i`, if `farthest < i`, then index `i` is unreachable → return `False`.
- Otherwise, update `farthest = max(farthest, i + nums[i])`.
At the end, check whether `farthest >= n - 1`.

**Key invariant:** before using `nums[i]` to extend range, index `i` must be reachable.

## Algorithm
1. Initialize `farthest = 0`.
2. Iterate `i` from `0` to `n-1`:
   - If `farthest < i`: return `False`
   - Update `farthest = max(farthest, i + nums[i])`
3. Return `True`

## Complexity
- **Time:** `O(n)`
- **Space:** `O(1)`

## Notes
- Use `<` (not `<=`) in the unreachable check, because `farthest == i` means you can reach `i` exactly.
