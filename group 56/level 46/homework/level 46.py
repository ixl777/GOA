numbers = [x for x in range(1, 11)]
squares = [x**2 for x in range(1, 6)]
evens = [x for x in range(1, 21) if x % 2 == 0]
words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
divisible_by_three = [x for x in range(1, 51) if x % 3 == 0]
words = ["tiny", "massive", "small", "gigantic"]
long_words = [word for word in words if len(word) > 4]
celsius = [0, 20, 30, 100]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
primes = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]