

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)


def main():
    number = int(input("what nuber should we calculate fib"))
    result = fib(number)
    print(f"fib of {number} is {result}")


main()
