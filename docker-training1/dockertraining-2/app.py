def factorial(n):
	if n < 0:
		return "negative num"
	elif n == 0:
		return 1
	else:
		result = 1
		for i in range(1, n + 1):
			result *= i
		return result
		
with open("factorials.txt", "w") as f:
	for i in range(1, 11):	
		fact = factorial(i)
		output_line = f"The factorial of {i} is {fact}\n"
		print(output_line.strip())
		f.write(output_line)
		
print("\nSuccessfully wrote factorials to factorials.txt")
