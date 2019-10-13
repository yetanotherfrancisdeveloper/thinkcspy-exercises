# This program allows you to compute the final amount (called Future Value)
# you will have after t years of compound interest on an initial investment P.

P = 10000    # Initial investment.
n = 12       # Number of times the interest is compounded per year.
r = 0.08     # Annual nominal interest rate.

t = int(input("For how many years will your investment be compounded for? "))     # Number of years.
futureValue = P * (1 + r/n) ** (n*t)
print("The Future Value of your investment after", t, "years will be:", futureValue)
