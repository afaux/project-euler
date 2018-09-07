# problem_3.py

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600,851,475,143?

def is_prime(n):
	# make sure n is a positive integer
	n = abs(int(n))

	# 1 and 0 are not prime
	if n < 2:
		return False

	# 2 is prime
	if n == 2:
		return True

	# all even numbers are prime
	if n % 2 == 0:
		return False

	# check if any remaining numbers are factors
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False

	return True

# set target
target = 600851475143

# max factor is square root
max = int(target ** 0.5)+1

# container for prime factors
factors = []

# check if odd numbers less than square root are factor
for factor in range(1, max, 2):
	if is_prime(factor) and target%factor==0:
		factors.append(factor)

# output prime factor
print factors
