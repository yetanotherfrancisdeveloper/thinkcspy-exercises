def seq3np1():
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    max_so_far = 0
    for i in range(1, 51):
        n = i
        iterations = 0
        while i != 1:
            if i % 2 == 0:
                i = i // 2
            else:
                i = i * 3 + 1
            iterations += 1
        result = i
        if max_so_far < iterations:
            max_so_far = iterations
        print("For " + str(n) + " we've got " + str(result) + " after " + str(iterations) + " iterations")
    return "The max number of iterations is " + str(max_so_far)


print(seq3np1())
