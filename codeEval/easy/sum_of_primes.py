def gen_primes():
    D, q = {}, 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


s, i = 0, 0
for p in gen_primes():
    if i == 1000:
        break
    s += p
    i += 1
print s
