class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out = []

        for key in arr2:
            i = 0
            print(arr1, key)
            while i < len(arr1):
                if arr1[i] == key:
                    to_move = arr1.pop(i)
                    out.append(to_move)
                else:
                    i += 1
        
        out = out + sorted(arr1)

        return out