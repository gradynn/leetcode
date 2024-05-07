class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextLargest = {}
        stack = []
        for num in nums2[::-1]:
            while stack and stack[len(stack) - 1] < num:
                stack.pop()
            if not stack:
                nextLargest[num] = -1
            else:
                nextLargest[num] = stack[len(stack) - 1]
            stack.append(num)
        
        out = []
        for num in nums1:
            out.append(nextLargest[num])
        return out