def prime_factors(n):
    i, factors = 2, []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(prime_factors(int(input())))
