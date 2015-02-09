from sys import stdin


print '\n'.join(
    ('Bad', 'Good')['010' in ln or '101' in ln]
    for i, ln in enumerate(stdin) if i
)
