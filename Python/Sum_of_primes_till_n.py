def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 0
    return n
n = int(input("Enter a number: "))
result = 0
for i in range(2, n + 1):
    result += is_prime(i)
print("Sum of all prime numbers up to", n, ":", result)
