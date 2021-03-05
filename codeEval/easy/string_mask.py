from sys import argv


with open(argv[1], "r") as test_cases:
    for test in test_cases:
        print(
            "".join(
                a if b == "0" else a.upper() for a, b in zip(*test.rstrip().split())
            )
        )
