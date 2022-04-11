from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set(self.unique(e) for e in emails))

    def unique(self, email: str) -> str:
        local, domain = email.split("@")
        real, *ignored = local.split("+", 1)
        return real.replace(".", "") + "@" + domain
