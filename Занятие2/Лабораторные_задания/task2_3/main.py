def pow_gen(base: int):
    result = 1
    while True:
        yield result
        result *= base


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
