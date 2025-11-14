n = int(input("Enter n: "))
if n < 0:
    print("Enter positive number")
else:
    def fib_recursive(n):
        if n <= 1:
            return n
        return fib_recursive(n-1) + fib_recursive(n-2)

    def fib_iterative(n):
        if n <= 1:
            return n
        a, b, c = 0, 1, 0  # three variables
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c

    print("Number by recursive:", fib_recursive(n))
    print("Number by non-recursive:", fib_iterative(n))
