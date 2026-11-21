import pandas as pd

# ==========================================
# EXERCISE 1: Load & Inspect
# ==========================================
# 1. Load "sandbox/googleplaystore.csv" using pd.read_csv()
# 2. Print the first 5 rows (.head()), column types (.info()), and shape (.shape)
# 3. Count how many empty values exist in each column (.isna().sum())






# ==========================================
# EXERCISE 2: Rename Columns & Pick What You Need
# ==========================================
# 1. Keep only these 6 columns: App, Category, Rating, Installs, Price, Last Updated
# 2. Rename "Last Updated" to "last_updated" and make all column names lowercase
#    (Hint: df.columns = df.columns.str.lower())


# ==========================================
# EXERCISE 3: Remove Duplicates & Empty Rows
# ==========================================
# 1. Check how many duplicate app names exist: df["app"].duplicated().sum()
# 2. Remove duplicate apps using .drop_duplicates(subset=["app"])
# 3. Drop rows where "rating" is missing using .dropna(subset=["rating"])


# ==========================================
# EXERCISE 4: Clean Messy Price Text into Numbers
# ==========================================
# 1. Remove the "$" sign from the "price" column using .str.replace("$", "", regex=False)
# 2. Convert "price" into numbers using pd.to_numeric(df["price"], errors="coerce")
#    (Note: 1 broken row has "Everyone" as price; errors="coerce" turns it into NaN)
# 3. Drop any row where "price" became NaN


# ==========================================
# EXERCISE 5: Clean the Installs Column
# ==========================================
# 1. Remove both "+" and "," from the "installs" column (e.g. "10,000+" -> "10000")
# 2. Convert "installs" into whole numbers (int or float)


# ==========================================
# EXERCISE 6: Filter Rows & Create a New Tag Column
# ==========================================
# 1. Create a smaller table called "paid_apps" keeping only rows where price > 0
# 2. Create a smaller table called "food_apps" keeping only category == "FOOD_AND_DRINK"
# 3. Add a new column called "price_tier": set to "Free" if price == 0, else "Paid"


# ==========================================
# EXERCISE 7: Fix Dates & Group Summary Numbers
# ==========================================
# 1. Convert "last_updated" into real dates using pd.to_datetime(df["last_updated"], errors="coerce")
# 2. Extract the year into a new column: df["year"] = df["last_updated"].dt.year
# 3. Use .groupby("category")["price"].mean() to find the average price per category,
#    and sort from highest to lowest using .sort_values(ascending=False)
# 4. Use .groupby("year")["app"].count() to count how many apps were updated each year