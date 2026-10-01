import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

def pareto_and_slater(a):
    pareto_res = []
    slater_res = []
    
    for i, point in enumerate(a):
        is_pareto = True
        is_slater = True
        
        for j, other in enumerate(a):
            if i == j:
                continue
                
            if (other[0] >= point[0] and other[1] >= point[1]) and (other[0] > point[0] or other[1] > point[1]):
                is_pareto = False
                
            if other[0] > point[0] and other[1] > point[1]:
                is_slater = False
                
            if not is_pareto and not is_slater:
                break
                
        if is_pareto:
            pareto_res.append(i)
        if is_slater:
            slater_res.append(i)
            
    return pareto_res, slater_res

def find(row, row_index):
    a = [list(divmod(i, 10)) for i in row]

    headers = [f"A{i + 1}" for i in range(len(a))]

    if len(a) < 30:
        table_rows = [
            ["Q1"] + [a_f[0] for a_f in a],
            ["Q2"] + [a_s[1] for a_s in a]
        ]

        print(f"{row_index + 1} рядок:")
        print(tabulate(table_rows, headers=headers, tablefmt="plain", stralign="center", numalign="center"))
        print("")

    else:
        print("Для рядка, що складається з рядків 1-3:")

    pareto, slater = pareto_and_slater(a)

    print("Множина оптимальних значень за Парето:", ", ".join(f"A{i + 1}" for i in pareto))
    print("Множина оптимальних значень за Слейтер:", ", ".join(f"A{i + 1}" for i in slater))

    a_n = np.array(a)
    mask_s = np.zeros(len(a), dtype=bool)
    mask_p = np.zeros(len(a), dtype=bool)
    mask_s[slater] = True
    mask_p[pareto] = True

    def connect(ax, points):
        sorted_indices = np.argsort(points[:, 0])
        
        for i in range(len(sorted_indices) - 1):
            idx_current = sorted_indices[i]
            idx_next = sorted_indices[i + 1]
            
            ax.plot([points[idx_current, 0], points[idx_next, 0]], [points[idx_current, 1], points[idx_next, 1]], color='red')

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    axs[0].scatter(a_n[~mask_s, 0], a_n[~mask_s, 1], color='blue')
    axs[0].scatter(a_n[mask_s, 0], a_n[mask_s, 1], color='red')
    connect(axs[0], a_n[mask_s])
    axs[0].set_title("Границя Слейтера")
    axs[0].plot()
    axs[0].grid(True)

    axs[1].scatter(a_n[~mask_p, 0], a_n[~mask_p, 1], color='blue')
    axs[1].scatter(a_n[mask_p, 0], a_n[mask_p, 1], color='red')
    connect(axs[1], a_n[mask_p])
    axs[1].set_title("Границя Парето")
    axs[1].plot
    axs[1].grid(True)

    plt.show()

rows = [
    [98, 90, 24, 90, 9, 81, 19, 36, 32, 55, 94, 4, 79, 69, 73, 76, 50, 55, 60, 42],
    [79, 84, 93, 5, 21, 67, 4, 13, 61, 54, 26, 59, 44, 2, 2, 6, 84, 21, 42, 68],
    [28, 89, 72, 8, 58, 98, 36, 8, 53, 48, 3, 33, 54, 48, 90, 33, 67, 46, 68, 29]
]

for i, row in enumerate(rows):
    find(row, i)
    print("")

all_rows = []
for sublist in rows:
    all_rows.extend(sublist)
find(all_rows, 0)