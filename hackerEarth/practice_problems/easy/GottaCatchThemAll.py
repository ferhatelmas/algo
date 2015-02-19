raw_input()
ls = enumerate(sorted(map(int, raw_input().split()), reverse=True))
print max(i + e for i, e in ls) + 2
