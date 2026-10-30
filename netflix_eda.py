# Import required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Libraries imported successfully!")
# Load Netflix dataset

df = pd.read_csv("netflix_titles.csv")

print("\nDataset loaded successfully!")

# Display first five records
print(df.head())
# Check dataset dimensions

print("\nDataset Shape:")
print(df.shape)

# Check column names

print("\nColumn Names:")
print(df.columns.tolist())

# Check dataset information

print("\nDataset Information:")
df.info()
# 1. Dataset Shape

print("\n--- Dataset Shape ---")
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])
# 2. Dataset Information

print("\n--- Dataset Information ---")
df.info()
# 3. Missing Values

print("\n--- Missing Values ---")
print(df.isnull().sum())
# 4. Duplicate Records

print("\n--- Duplicate Records ---")
print("Total Duplicate Rows:", df.duplicated().sum())
# 5. Unique Values

print("\n--- Unique Values ---")

print("Content Types:")
print(df["type"].unique())

print("\nRatings:")
print(df["rating"].unique())

print("\nRelease Years:")
print(df["release_year"].nunique())
# 6. Statistical Summary

print("\n--- Statistical Summary ---")
print(df.describe(include="all"))
# 7. Dataset Verification

print("\n--- Dataset Verification ---")

print("Dataset Shape:", df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\nContent Type Distribution:")
print(df["type"].value_counts(dropna=False))

print("\nColumn Names:")
print(df.columns.tolist())
# 8. Data Cleaning

print("\n--- Data Cleaning ---")

# Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Fill missing director and cast values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")

# Fill missing country values
df["country"] = df["country"].fillna("Unknown")

# Remove rows with missing essential information
df.dropna(subset=["date_added", "duration", "rating"], inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDataset Shape After Cleaning:")
print(df.shape)

print("\nData Cleaning Completed!")
print(df.head(10))
print(df["type"].value_counts())
print(df.shape)
# 9. Movies vs TV Shows Analysis

import matplotlib.pyplot as plt
import os

print("\n--- Movies vs TV Shows Analysis ---")

# Count Movies and TV Shows
content_counts = df["type"].value_counts()

# Create bar chart
plt.figure(figsize=(8, 5))

plt.bar(content_counts.index, content_counts.values)

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.grid(axis="y", linestyle="--", alpha=0.5)

# Save chart
os.makedirs("visualizations", exist_ok=True)

plt.savefig("visualizations/movies_vs_tv_shows.png",
            dpi=300, bbox_inches="tight")

plt.show()

print("Movies vs TV Shows chart saved successfully!")
# 10. Content Ratings Analysis

print("\n--- Content Ratings Analysis ---")

# Count content ratings
rating_counts = df["rating"].value_counts()

# Create bar chart
plt.figure(figsize=(10, 6))

rating_counts.plot(kind="bar")

plt.title("Distribution of Content Ratings on Netflix")
plt.xlabel("Content Rating")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

# Save chart
plt.savefig("visualizations/content_ratings.png",
            dpi=300, bbox_inches="tight")

plt.show()

print("Content Ratings chart saved successfully!")
# 11. Top 10 Countries Analysis

print("\n--- Top 10 Countries Analysis ---")

# Split countries because some titles have multiple countries
countries = df["country"].dropna().str.split(", ").explode()

# Count titles by country
country_counts = countries.value_counts()

# Select top 10 countries
top_countries = country_counts.head(10)

# Create bar chart
plt.figure(figsize=(10, 6))

top_countries.plot(kind="bar")

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

# Save chart
plt.savefig("visualizations/top_10_countries.png",
            dpi=300, bbox_inches="tight")

plt.show()

print("\nTop 10 Countries:")
print(top_countries)

print("Country Analysis chart saved successfully!")
# 12. Content Release Trends Analysis

print("\n--- Content Release Trends ---")

# Count titles by release year
year_counts = df["release_year"].value_counts().sort_index()

# Create line chart
plt.figure(figsize=(12, 6))

plt.plot(year_counts.index, year_counts.values,
         marker="o", linewidth=2)

plt.title("Netflix Content Release Trends Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

# Save chart
plt.savefig("visualizations/release_trends.png",
            dpi=300, bbox_inches="tight")

plt.show()

print("\nContent Release Trends:")
print(year_counts.tail(15))

print("Release Trends chart saved successfully!")
# 13. Key Findings and Insights

print("\n========== KEY FINDINGS ==========")

# 1. Total Movies and TV Shows
content_counts = df["type"].value_counts()

print("\n1. Content Distribution:")
print("Total Movies:", content_counts.get("Movie", 0))
print("Total TV Shows:", content_counts.get("TV Show", 0))

# 2. Most Common Content Rating
print("\n2. Most Common Content Rating:")
print(df["rating"].mode()[0])

# 3. Top 5 Countries
countries = df["country"].dropna().str.split(", ").explode()
print("\n3. Top 5 Content Producing Countries:")
print(countries.value_counts().head(5))

# 4. Most Active Release Year
year_counts = df["release_year"].value_counts()

print("\n4. Year with Maximum Content Releases:")
print(year_counts.idxmax())

# 5. Total Titles
print("\n5. Total Titles in Dataset:")
print(len(df))

print("\n========== ANALYSIS COMPLETED ==========")