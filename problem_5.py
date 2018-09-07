# problem_5.py

# 2520 is the smallest number that can be divided by each of 
# the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?


first = 1
last = 20

max = 1
min = 0
temp = 0

for number in range(last, first-1, -1):
	if max % number > 0:
		max = max * number
		
for number_1 in range(last, first-1, -1):
	for number_2 in range(number_1, first-1, -1):
		if max%number_2 > 0:
			temp+1
	if temp == 0:
		min = max/number_1

print min