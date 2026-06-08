import pandas as pd
import random

names = [
    "Ram", "Ravi", "Priya", "Anu", "Kiran", "John", "Sita", "Arjun",
    "Meena", "Rahul", "Akash", "Neha", "Rohit", "Pooja", "Vikram",
    "Sneha", "Ajay", "Divya", "Nikhil", "Kavya"
]

data = []

for i in range(1, 101):

    attendance = random.randint(60, 100)

    if attendance > 85:
        math = random.randint(75, 100)
        science = random.randint(75, 100)
        english = random.randint(75, 100)
    else:
        math = random.randint(50, 85)
        science = random.randint(50, 85)
        english = random.randint(50, 85)

    data.append([
        i,
        random.choice(names),
        math,
        science,
        english,
        attendance
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Student_ID",
        "Name",
        "Math",
        "Science",
        "English",
        "Attendance"
    ]
)

df.to_csv("student_data.csv", index=False)

print("100 student records generated successfully!")