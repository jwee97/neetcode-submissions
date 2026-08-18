class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = set()
        for i in nums:
            ans.add(i)
        
        longest = 0
        for num in ans:
            if (num - 1) not in ans:
                length = 1
                while (num + length) in ans:
                    length += 1
                longest = max(length, longest)
        
        return longest

        