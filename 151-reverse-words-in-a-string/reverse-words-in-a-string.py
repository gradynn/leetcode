class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        
        in_word, word = False, ""
        for c in s:
            if c != ' ':
                in_word = True
                word += c
            elif word and c == ' ':
                words.append(word)
                word = ""
                in_word = False
        if word != "":
            words.append(word)
        
        return ' '.join(words[::-1])
        