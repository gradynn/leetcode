class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_to_s = {}
        s_to_p = {}

        s_arr = s.split(' ')

        if len(s_arr) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in p_to_s.keys() and s_arr[i] not in s_to_p.keys():
                p_to_s[pattern[i]] = s_arr[i]
                s_to_p[s_arr[i]] = pattern[i]
            else:
                if pattern[i] in p_to_s.keys() and p_to_s[pattern[i]] != s_arr[i]:
                    return False
                if s_arr[i] in s_to_p.keys() and s_to_p[s_arr[i]] != pattern[i]:
                    return False

        return True

