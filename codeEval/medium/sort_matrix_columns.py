import sys


with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        ls = [map(int, e.split()) for e in test_case.split('|')]
        print(
            ' | '.join(
                ' '.join(str(e) for e in row)
                for row in zip(*sorted(zip(*ls)))
            )
        )
