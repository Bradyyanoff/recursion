def loop_factorial(n):
    result = 1
    for number in range(1, n):
        result = result * number
    return n*result
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

def main():
    number = int(input("what number shall we find the factorial for:"))
    result = fact(number)
    loop = loop_factorial(number)
    print(f"the factorial was {result}")
    print(f"the loop version was {loop}")

main()