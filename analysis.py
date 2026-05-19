import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv", sep=";")

# Show first rows
print(df.head())

# Count Movies vs TV Shows
type_counts = df['type'].value_counts()

print(type_counts)

# Plot chart
type_counts.plot(kind='bar')

plt.title("Movies vs TV Shows on Netflix")

plt.xlabel("Type")

plt.ylabel("Count")

plt.show()