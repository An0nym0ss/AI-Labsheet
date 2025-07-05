import math
from collections import Counter

DATASET = [
    # age, income, jeans_type
    (18, 12000, "Skinny"),
    (19, 12500, "Skinny"),
    (20, 14000, "Skinny"),
    (21, 14500, "Skinny"),
    (22, 15000, "Skinny"),
    (23, 16000, "Skinny"),
    (24, 16500, "Skinny"),
    (25, 17000, "Regular"),
    (26, 18000, "Regular"),
    (27, 18500, "Regular"),
    (28, 20000, "Regular"),
    (29, 20500, "Regular"),
    (30, 21000, "Regular"),
    (31, 22000, "Regular"),
    (32, 22500, "Bootcut"),
    (33, 24000, "Bootcut"),
    (34, 24500, "Bootcut"),
    (35, 25000, "Bootcut"),
    (36, 26000, "Bootcut"),
    (37, 26500, "Bootcut"),
    (38, 27000, "Bootcut"),
    (39, 28000, "Bootcut"),
    (40, 28500, "Relaxed"),
    (41, 30000, "Relaxed"),
    (42, 30500, "Relaxed"),
    (43, 31000, "Relaxed"),
    (44, 32000, "Relaxed"),
    (45, 32500, "Relaxed"),
    (46, 33000, "Relaxed"),
    (47, 34000, "Relaxed"),
    (48, 34500, "Loose"),
    (49, 35000, "Loose"),
    (50, 36000, "Loose"),
    (51, 36500, "Loose"),
    (52, 37000, "Loose"),
    (53, 38000, "Loose"),
    (54, 38500, "Loose"),
    (55, 39000, "Loose"),
    (56, 40000, "Loose"),
    (57, 40500, "Loose"),
    (58, 41000, "Loose"),
    (59, 41500, "Loose"),
    (60, 42000, "Loose"),
]

K = 3

def compute_distance(age1, income1, age2, income2):
    return math.sqrt((age1 - age2) ** 2 + (income1 - income2) ** 2)

def predict_jeans_type(input_age, input_income, k=K):
    # Lazy learning: no model, compute on demand
    neighbors = []
    for age, income, jeans_type in DATASET:
        dist = compute_distance(input_age, input_income, age, income)
        neighbors.append((dist, jeans_type))
    neighbors.sort(key=lambda x: x[0])
    top_k = [jeans for _, jeans in neighbors[:k]]
    most_common = Counter(top_k).most_common(1)[0][0]
    return most_common

if __name__ == "__main__":
    age = int(input("Enter age: "))
    income = int(input("Enter monthly income (NPR): "))
    result = predict_jeans_type(age, income)
    print(f"\nPredicted jeans type: {result}")