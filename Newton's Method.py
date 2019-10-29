def newton_sqrt(n):
    approx = 0.5 * n
    better_approx = 0.5 * (approx + n / approx)
    times = 1
    while approx != better_approx:
        approx = better_approx
        better_approx = 0.5 * (approx + n / approx)
        times += 1
    print(times)
    return better_approx


print(newton_sqrt(100))
