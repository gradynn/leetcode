class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []

        path_arr = [d.replace('/', '') for d in path.split('/') if d != '']
        for d in path_arr:
            if len(st) > 0 and d == "..":
                st.pop()
            elif d != ".." and d != '.':
                st.append(d)
        
        return '/' + '/'.join(st)