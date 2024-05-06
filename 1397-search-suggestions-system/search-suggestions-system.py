class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        sortedProds = sorted(products)

        out = []
        l, r = 0, len(products) - 1
        for i in range(1, len(searchWord) + 1):
            def isNotPrefix(prefix, word):
                if len(word) < len(prefix):
                    return True
                return word[0:len(prefix)] != prefix
            
            while l <= r and isNotPrefix(searchWord[0:i], sortedProds[l]):
                l += 1
            while l <= r and isNotPrefix(searchWord[0:i], sortedProds[r]):
                r -= 1

            if (r - l) + 1 > 3:
                out.append(sortedProds[l:(l + 3)])
            else:
                out.append(sortedProds[l:(r + 1)])
        
        return out 