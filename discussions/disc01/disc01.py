def wears_jacket_with_if(temp, raining):
	"""
	>>> wears_jacket_with_if(90, False)
	False
	>>> wears_jacket_with_if(40, False)
	True
	>>> wears_jacket_with_if(100, True)
	True
	"""
	return True if temp < 60 or raining == True else False


def is_prime(n):
	"""
	>>> is_prime(10)
	False
	>>> is_prime(7)
	True
	"""
	counter = 2
	while counter < n:
		if n % counter == 0:
			return False
		counter += 1
	return True