def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        result = Fibonacci(n - 1) + Fibonacci(n - 2)
        return result


n = int(input("Enter the n to learn n-th fibonacci number: "))

print(Fibonacci(n))
