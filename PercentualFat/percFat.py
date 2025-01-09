# JSON Example
revenue = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Others": 19849.53,
}

totalRevenue = sum(revenue.values())

for state, value in revenue.items():
    percentage = (value / totalRevenue) * 100
    print(f"{state} represents {percentage:.2f}% of the revenue")
