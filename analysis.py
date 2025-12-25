import pandas as pd

# CSV dosyasını oku
df = pd.read_csv("data.csv")

# Veriyi göster
print("Student Grades:\n")
print(df)

# Ders ortalamaları
print("\nCourse Averages:")
print("Math:", df["math"].mean())
print("Physics:", df["physics"].mean())
print("Computer Science:", df["cs"].mean())

# En başarılı öğrenci
df["average"] = df[["math", "physics", "cs"]].mean(axis=1)
top_student = df.loc[df["average"].idxmax()]

print("\nTop Student:")
print(top_student)
import matplotlib.pyplot as plt

# Ders ortalamalarını listeye al
courses = ["Math", "Physics", "Computer Science"]
averages = [
    df["math"].mean(),
    df["physics"].mean(),
    df["cs"].mean()
]

# Grafik çiz
plt.bar(courses, averages)
plt.title("Course Averages")
plt.ylabel("Average Score")
plt.xlabel("Courses")
plt.show()
