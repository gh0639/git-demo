def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 10, 13]
prime_numbers = []

for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)

print("Prime numbers in the list:", prime_numbers)