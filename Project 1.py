import matplotlib.pyplot as plt

students = [
    ["Vaishnavi", 90, 95, 93],
    ["Tanishk", 89, 90, 85],
    ["Rohan", 45, 50, 48],
    ["Rehan", 72, 78, 75],
    ["Shri", 80, 84, 81]
]

print("------Student performance report-------")
topper = ""
highest_avg = 0
pass_count = 0

names = []
averages = []

for student in students:
    name = student[0]
    total = student[1] + student[2] + student[3]
    avg = total / 3

    names.append(name)
    averages.append(avg)

    if avg >= 40:
        status = "PASS"
        pass_count += 1
    else:
        status = "FAIL"

    if avg > highest_avg:
        highest_avg = avg
        topper = name

    print(f"{name:<8} | Total:{total} | Avg: {avg:.1f}% | {status}")

pass_percentage = (pass_count / len(students)) * 100
print("------------------")
print(f"Class Topper : {topper} ({highest_avg:.1f})")
print(f"Class pass rate: {pass_percentage:.1f}%")

# --- Simple Graph (Just 4 lines) ---
plt.bar(names, averages)
plt.title("Student Average Marks")
plt.ylabel("Average %")
plt.show()
