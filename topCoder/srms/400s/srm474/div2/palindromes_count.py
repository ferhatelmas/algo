class PalindromesCount:
    def count(self, A, B):
        def is_palindrome(s):
            return s == s[::-1]

        return sum(is_palindrome(A[:i] + B + A[i:]) for i in xrange(len(A) + 1))
