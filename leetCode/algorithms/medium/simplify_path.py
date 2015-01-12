class Solution:
    def simplifyPath(self, path):
        ls = []
        for e in path.split('/'):
            if not e or e == '.':
                continue
            if e == '..':
                if ls:
                    ls.pop()
            else:
                ls.append(e)
        return '/' + '/'.join(ls)