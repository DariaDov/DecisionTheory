import pandas as pd

additional_1 = {
    "H1": [95, 0, 0, 52, 52, 68, 42, 42, 42, 68, 68, 52, 0],
    "H2": [75, 76, 76, 0, 0, 54, 28, 28, 28, 54, 54, 0, 76],
    "H3": [50, 124, 124, 86, 86, 0, 28, 28, 28, 0, 0, 86, 124],
    "H4": [30, 124, 124, 86, 86, 54, 0, 0, 0, 54, 54, 86, 124],
    "H5": [30, 124, 124, 86, 86, 54, 14, 14, 14, 54, 54, 86, 124],
    "H6": [20, 124, 124, 100, 100, 68, 42, 42, 42, 68, 68, 100, 124]
}

additional_2 = {
    "H1": [95, 0, 0, 28, 28, 68, 42, 42, 42, 68, 68, 28, 0],
    "H2": [75, 44, 44, 0, 0, 54, 28, 28, 28, 54, 54, 0, 44],
    "H3": [50, 68, 68, 38, 38, 0, 28, 28, 28, 0, 0, 38, 68],
    "H4": [30, 68, 68, 38, 38, 54, 0, 0, 0, 54, 54, 38, 68],
    "H5": [30, 68, 68, 38, 38, 54, 14, 14, 14, 54, 54, 38, 68],
    "H6": [20, 68, 68, 52, 52, 68, 42, 42, 42, 68, 68, 52, 68]
}

probability_2 = [1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12]

probability_3_w = [1/3, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/3]
probability_3_s = [0, 0, 1/3, 1/3, 1/3, 0, 0, 0, 0, 0, 0, 0]
probability_3_sum = [0, 0, 0, 0, 0, 1/3, 1/3, 1/3, 0, 0, 0, 0]
probability_3_a = [0, 0, 0, 0, 0, 0, 0, 0, 1/3, 1/3, 1/3, 0]

probability_4 = [1/6, 1/6, 1/18, 1/18, 1/18, 1/18, 1/18, 1/18, 1/18, 1/18, 1/18, 1/6]
probability_5 = [31/365, 28/365, 31/365, 6/73, 31/365, 6/73, 31/365, 31/365, 6/73, 31/365, 6/73, 31/365]

results = {}

def calculate(a, p):
    for key, values in a.items():
        cost = values[0]
        E = sum((-cost -values[i]) * p[i - 1] for i in range(1, 13))
        results[key] = E
        print(f"E[U({key})] = {E:.2f}")

    min_strategy = max(results, key=results.get)
    print(f"Найкраща стратегія: {min_strategy} = {results[min_strategy]:.2f}\n")


print("За 12 місяців:")
calculate(additional_1, probability_2)

print("Зима:")
calculate(additional_1, probability_3_w)
print("Весна:")
calculate(additional_1, probability_3_s)
print("Літо:")
calculate(additional_1, probability_3_sum)
print("Осінь:")
calculate(additional_1, probability_3_a)

print("Зима х3:")
calculate(additional_1, probability_4)

print("За 12 місяців (за кількістю днів):")
calculate(additional_1, probability_5)

print("За 12 місяців (зменш. вартість):")
calculate(additional_2, probability_2)