def example() -> int:
    sum = 0
    for i in [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]:
        if i % 2 == 0:
            sum += i
    return sum


def implementation() -> int:
    sum = 0
    previous = 0
    fib = 1
    while fib < 4_000_000:
        previous, fib = fib, previous + fib
        if fib % 2 == 0 and fib < 4_000_000:
            sum += fib
    return sum


if __name__ == "__main__":
    implementation()
