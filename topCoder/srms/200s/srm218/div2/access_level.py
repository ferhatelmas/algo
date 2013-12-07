class AccessLevel:
    def canAccess(self, rights, minPermission):
        return ''.join(map(lambda i: 'A' if i>= minPermission else 'D', rights))
