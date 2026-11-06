# EC2 - First dataset
# I am in Grade 11. This is my first test.
# Question: Did people panic buy food in March 2020, when COVID started?
# Data: Statistics Canada, The Daily, Retail trade, March 2020, released May 22, 2020.
# Link: https://www150.statcan.gc.ca/n1/daily-quotidien/200522/dq200522a-eng.htm

import pandas as pd

# Step 1: Read the file I made from the StatCan numbers.
df = pd.read_csv("data/march_2020_retail.csv")

print("Rows in my file:")
print(len(df))
print()
print(df)

# Step 2: Get the total retail change. I need it to compare the other stores to it.
total_change = -10.0
print()
print("Total retail change in March 2020 was", total_change, "percent.")

# Step 3: Make a panic score.
# Panic score = how much a store type changed, minus the total change.
# If the score is high and positive, that store went up a lot more than retail as a whole.
# That is what panic buying looks like.
df["panic_score"] = df["change_percent_march_2020"] - total_change

# Step 4: Sort the table, biggest panic score first.
df = df.sort_values("panic_score", ascending=False)

print()
print("Table sorted by panic score:")
print(df)

# Step 5: Save the clean table.
df.to_csv("data/march_2020_retail_clean.csv", index=False)
print()
print("Saved clean file to data/march_2020_retail_clean.csv")

# Step 6: My answer in plain words.
food_row = df[df["store_type"] == "Food and beverage stores"].iloc[0]
print()
print("Food and beverage stores went up by", food_row["change_percent_march_2020"], "percent.")
print("Total retail went down by 10.0 percent.")
print("So food stores went up a lot while most retail went down.")
print("That fits panic buying. People stocked up on food.")
print("This is only 4 rows. It is a first test, not the full 200,000 point study yet.")
