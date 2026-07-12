# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display DataFrame shape
print("\nShape of DataFrame:", df.shape)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Create a Total_Sales column
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Display updated DataFrame
print("\nUpdated Data:")
print(df)

# Group data by Category
category_sales = df.groupby("Category")["Total_Sales"].sum()

print("\nSales by Category:")
print(category_sales)

# Plot Bar Chart
plt.figure(figsize=(6,4))
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.grid(axis="y")
plt.show()

# Filter rows where Total Sales > 10000
filtered = df[df["Total_Sales"] > 10000]

print("\nProducts with Total Sales greater than 10000:")
print(filtered)