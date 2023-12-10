fibonacciNums = dict()
fibonacciNums[1] = 1
fibonacciNums[2] = 1


def Fibonacci(n):
    if n in fibonacciNums:
        return fibonacciNums[n]
    else:
        result = Fibonacci(n - 1) + Fibonacci(n - 2)
        fibonacciNums[n] = result
        return result


n = int(input("Enter the n to learn n-th fibonacci number: "))

print(Fibonacci(n))
