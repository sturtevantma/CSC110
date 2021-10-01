def even_fib(a: int, b: int, n: int) -> int:
    lis = [a, b]
    for _ in range(n):
        lis.append(lis[-1] + lis[-2])
    return sum([i for i in lis if i % 2 == 0])

print(even_fib(1, 2, 4_000_000))