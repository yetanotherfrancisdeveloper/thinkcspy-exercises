nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# a. Write a loop that prints each of the numbers on a new line.
for i in nums:
    print(i)

# b. Write a loop that prints each number and its square on a new line.
numsAndSquares = {}

for x in nums:
    numsAndSquares[x] = x ** 2

for k, v in numsAndSquares.items():
    print("The square of", k, "is equal to:", v)
