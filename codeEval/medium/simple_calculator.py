import sys, re

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    res = eval(
        re.sub(
            r"(\d+(\.\d+)?)",
            lambda e: str(float(e.group(1))),
            test.strip().replace("^", "**"),
        )
    )
    print("%.5f" % res).rstrip("0").rstrip(".")
test_cases.close()
