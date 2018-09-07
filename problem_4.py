# problem_4.py

# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
	if n == 1:
		return True

	ones = n % 10
	tens = (n % 100 - ones)/10
	hundreds = (n % 1000 - tens - ones)/100
	thousands = (n % 10000 - hundreds - tens - ones)/1000
	ten_thousands = (n % 100000 - thousands - hundreds - tens - ones)/10000
	hundred_thousands = (n % 1000000 - ten_thousands - thousands - hundreds - tens - ones)/100000

	if n > 10 and n < 100 and ones == tens:
		return True

	if n > 100 and n < 1000 and ones == thousands:
		return True

	if n > 1000 and n < 10000 and ones == thousands and tens == hundreds:
		return True

	if n > 10000 and n < 100000 and ones == ten_thousands and tens == thousands:
		return True

	if n > 100000 and n < 1000000 and ones == hundred_thousands and tens == ten_thousands and hundreds == thousands:
		return True

	return False

max_palindrome = 0

for number_1 in range(999,99, -1):
	for number_2 in range(999,99,-1):
		product = number_1 * number_2
		if is_palindrome(product) and product > max_palindrome:
			max_palindrome = product
			one = number_1
			two = number_2

print "%d * %d = %d" % (one, two, max_palindrome)