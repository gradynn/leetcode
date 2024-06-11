class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        arr1_counts = defaultdict(int)
        remainder = []
        for n in arr1:
            if n not in arr2_set:
                remainder.append(n)
            else:
                arr1_counts[n] += 1
        
        out = []
        for n in arr2:
            for i in range(arr1_counts[n]):
                out.append(n)

        return out + sorted(remainder)