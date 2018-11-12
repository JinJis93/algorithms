int_a = 3141592653589793238462643383279502884197169399375105820974944592
int_b = 2718281828459045235360287471352662497757247093699959574966967627


def multiply(int1: int, int2: int):
	# make as string type
	str_1 = str(int1)
	str_2 = str(int2)

	# if digit is 1, finish recursive
	if len(str_1) == 1 and len(str_2) == 1:
		sum_up = 0
		for i in range(int(str_1)):
			sum_up += int2
		return int(sum_up)

	# add "0" and get digit accordingly
	str_1, str_2, digit = filter_even_max_lenghted_num(str_1, str_2)

	half_digit = int(digit / 2)
	a = int(str_1[:half_digit])
	b = int(str_1[half_digit:])
	c = int(str_2[:half_digit])
	d = int(str_2[half_digit:])

	coeff = int(10 ** half_digit)

	return int(
		coeff * (coeff - 1) * multiply(a, c) + coeff * multiply(a + b, c + d) + (1 - coeff) * multiply(b, d)
	)


def filter_even_max_lenghted_num(str_1: str, str_2: str):
	# decide max len
	if len(str_1) >= len(str_2):
		diff = len(str_1) - len(str_2)
		if len(str_1) % 2 == 0:
			return str_1, "0" * diff + str_2, len(str_1)
		else:
			return "0" + str_1, "0" * (diff + 1) + str_2, len(str_1) + 1

	else:
		diff = len(str_2) - len(str_1)
		if len(str_2) % 2 == 0:
			return "0" * diff + str_1, str_2, len(str_2)
		else:
			return "0" * (diff + 1) + str_1, "0" + str_2, len(str_2) + 1


print(multiply(int_a, int_b))
