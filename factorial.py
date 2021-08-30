def factorial(n):
    if n==0:
        return 1
    product = 1
    for i in range(1, n+1):
        product*=i
    return product