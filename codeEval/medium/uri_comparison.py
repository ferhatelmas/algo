import sys
from urlparse import urlparse
from urllib import unquote


def compare(a, b):
    return (
        a.scheme.lower() == b.scheme.lower()
        and a.hostname == b.hostname
        and (a.port or 80) == (b.port or 80)
        and unquote(a.path) == unquote(b.path)
    )


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print compare(*map(urlparse, test.strip().split(";")))
test_cases.close()
