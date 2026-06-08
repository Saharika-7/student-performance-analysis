import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_data.csv")

df["Average"] = (
    df["Math"] +
    df["Science"] +
    df["English"]
) / 3

print(df)

print("\nMean Scores:")
print(df[["Math","Science","English"]].mean())

print("\nMedian Scores:")
print(df[["Math","Science","English"]].median())

print("\nStandard Deviation:")
print(df[["Math","Science","English"]].std())


# ATTENDANCE ANALYSIS STARTS HERE

high_attendance = df[df["Attendance"] > 85]

print("\nStudents with Attendance > 85%")
print(high_attendance)

print("\nAverage Score of High Attendance Students")
print(high_attendance["Average"].mean())

# ATTENDANCE ANALYSIS ENDS HERE


subjects = ["Math","Science","English"]

average_scores = df[subjects].mean()

plt.bar(subjects, average_scores)

plt.title("Average Subject Scores")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.savefig("bar_chart.png")
plt.show()
plt.figure()

plt.scatter(
    df["Attendance"],
    df["Average"]
)

plt.title("Attendance vs Average Score")
plt.xlabel("Attendance")
plt.ylabel("Average Score")

plt.savefig("attendance_vs_score.png")

plt.show()
plt.figure(figsize=(8,5))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)

plt.title("Correlation Heatmap")

plt.savefig("heatmap.png")

plt.show()
plt.figure(figsize=(8,5))

sns.boxplot(
    data=df[["Math", "Science", "English"]]
)

plt.title("Score Distribution by Subject")

plt.savefig("boxplot.png")

plt.show()