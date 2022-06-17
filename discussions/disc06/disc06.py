def memory(n):
	"""Write a function that takes in a number n and returns a one-argument function.
	The returned function takes in a function that is used to update n.
	It should return the updated n.

	>>> f = memory(10)
	>>> f(lambda x: x * 2)
	20
	>>> f(lambda x: x - 7)
	13
	>>> f(lambda x: x > 5)
	True
	"""
	def f(g):
		nonlocal n
		n = g(n)
		return n
	return f


def group_by(s, fn):
	"""Write a function that takes in a sequence s and a function fn 
	and returns a dictionary.

	>>> group_by([12, 23, 14, 45], lambda p: p // 10)
	{1: [12, 14], 2: [23], 4: [45]}
	>>> group_by(range(-3, 4), lambda x: x * x)
	{9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
	"""
	grouped = {}
	for element in s:
		key = fn(element)
		if key in grouped:
			grouped[key].append(element)
		else:
			grouped[key] = [element]
	return grouped


def add_this_many(x, el, s):
	"""Adds el to the end of s the number of times x occurs in s.
	>>> s = [1, 2, 4, 2, 1]
	>>> add_this_many(1, 5, s)
	>>> s
	[1, 2, 4, 2, 1, 5, 5]
	>>> add_this_many(2, 2, s)
	>>> s
	[1, 2, 4, 2, 1, 5, 5, 2, 2]
	"""
	for element in range(len(s)):
		if s[element] == x:
			s.append(element)
	return s


def filter(iterable, fn):
	"""
	>>> is_even = lambda x: x % 2 == 0
	>>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
	[0, 2, 4]
	>>> all_odd = (2*y-1 for y in range(5))
	>>> list(filter(all_odds, is_even))
	[]
	>>> naturals = (n for n in range(1, 100))
	>>> s = filter(naturas, is_even)
	>>> next(s)
	2
	>>> next(s)
	4
	"""
	for x in iterable:
		if fn(x):
			yield x


def merge(a, b):
	"""
	>>> def sequence(start, step):
	...		while True:
	...			yield start
	...			start += step
	>>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
	>>> b = sequence(3, 2) # 2, 3, 5, 7, 9, 11, 13, 15, ...
	>>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
	>>> [next(result) for _ in range(10)]
	[2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
	"""
	element_a, element_b = next(a), next(b)
	while True:
		if element_a == element_b:
			yield element_a
			element_a, element_b = next(a), next(b)
		elif element_a < element_b:
			yield element_a
			element_a, element_b = next(a)
		else:
			yield element_b
			element_b = next(b)





