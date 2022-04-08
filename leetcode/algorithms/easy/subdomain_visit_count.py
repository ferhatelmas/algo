from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = {}
        for item in cpdomains:
            c, d = item.split()
            c = int(c)
            parts = d.split(".")
            for i, _ in enumerate(parts):
                domain = ".".join(parts[i:])
                domains[domain] = c + domains.get(domain, 0)
        return ["{} {}".format(v, k) for k, v in domains.items()]
