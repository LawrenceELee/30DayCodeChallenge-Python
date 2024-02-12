'''
Write a function that checks if a number is prime
'''

'''
Ideas/algorithms:
1. sieve of eratosthenes
2. trial division
3. fermat's little theorem
4. miller-rabin primality test
5. solovay-strassen primality test
6. lucas-lehmer primality test
7. elliptic curve primality test
8. AKS primality test
9. Adleman-Pomerance-Rumely primality test
'''

# brute force approach to check if a number is prime or not
# time complexity: O(n)
# space complexity: O(1)
def is_prime_brute_force(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# this generates a list of prime numbers up to n
# but there are faster algorithms to check if a number is prime
def is_prime_seive_(n):
    # Create a list of True values of length n
    primes = [True] * n

    # 0 and 1 are not prime
    primes[0] = primes[1] = False
    
    # Loop through the list
    for i in range(2, int(n ** 0.5) + 1):
        # we only have to go to math.sqrt(n)
        # because if n is divisible by a number greater than its square root,
        # then it is divisible by something smaller than its square root
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    return primes

primes_seive = is_prime_seive_(100)
#print(f"primes_seive: {primes_seive}")

primes = []
for i, is_prime in enumerate(primes_seive):
    if is_prime:
        primes.append(i)
print(f"primes: {primes}")

n = 13
print(f"{n} is prime: {primes_seive[n]}")
n = 15
print(f"{n} is prime: {primes_seive[n]}")
n = 15
print(f"{n} is prime: {primes_seive[n]}")