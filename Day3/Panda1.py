
import pandas as pd
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'Age': [25, 32, 29, 41, 37, 45, 26, 38],
    'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
    'Experience': [2, 7, 5, 15, 10, 20, 3, 12]
}

df = pd.DataFrame(data)
grouped = df.groupby('Department')

print("Average Salary by Department: ")
print(f" {grouped['Salary'].mean().to_string()}")

print("Highest salary by Department:")
print(f" {grouped['Salary'].max().to_string()}")

cnt = 0
for salary, experience in zip(df['Salary'], df['Experience']):
    if salary > 65000 and experience > 5:
        cnt += 1

print(f"Number of employees with salary > 65000 and experience > 5 years: {cnt}")

Seniority = []
for experience in df['Experience']:
    if (experience > 10):
        Seniority.append('Senior')
    elif (experience > 5):
        Seniority.append('Mid-level')
    else:
        Seniority.append('Junior')
df['Seniority'] = Seniority
print(df)

for department, group in grouped:
    if department == 'IT':
        sorted_group = group.sort_values(by='Salary', ascending=False)
        print("Sorted IT Department Employees by Salary (Descending):")
        print(sorted_group)