def example() -> int:
    sum = 0
    for i in range(10):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


def implementation() -> int:
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


if __name__ == "__main__":
    implementation()
