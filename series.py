def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n = int(input('> '))
    print(fibonacci(n))


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    #if n == 2:


    return lucas(n - 1) + lucas(n - 2)

if __name__ == '__main__':
    n = int(input('> '))
    print(lucas(n))

def sum_series(n):
    if n < 0:
        print("Number larger than 0 please")
    if n == 1:
        return 2
    if n == 2:
        return 2

    return fibonacci(n-2) + fibonacci(n-1) + lucas(n-2) + lucas(n-1)

if __name__ == '__main__':
    n = int(input('> '))
    print(f"The{n}th fibonacci numer is {fibonacci(int(n))}, the {n}th lucas number is {lucas(int(n))}, the sum of those two is {sum_series(int(n))}")
