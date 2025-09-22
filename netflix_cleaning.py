import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("netflix_titles.csv")

# Step 2: Look at first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())
# Remove exact duplicate rows
print("\nNumber of duplicate rows before cleaning:", df.duplicated().sum())
df = df.drop_duplicates().reset_index(drop=True)
print("Number of duplicate rows after cleaning:", df.duplicated().sum())
# Normalize column names
import re
df.columns = [re.sub(r'[^\w]', '_', c.strip().lower()) for c in df.columns]

# Trim whitespace in all text columns
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

print("\nColumn names after cleaning:")
print(df.columns)
# Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

# For date_added, convert to datetime, missing dates become NaT
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce', infer_datetime_format=True)

print("\nMissing values after filling:")
print(df.isnull().sum())
import re

# Parse duration into number and unit
def parse_duration(x):
    if pd.isna(x) or x == '':
        return pd.NA, pd.NA
    s = str(x).strip()
    m = re.search(r'(\d+)', s)
    if not m:
        return pd.NA, pd.NA
    num = int(m.group(1))
    if 'min' in s.lower():
        unit = 'Minutes'
    elif 'season' in s.lower():
        unit = 'Seasons'
    else:
        unit = pd.NA
    return num, unit

df[['duration_int','duration_unit']] = df['duration'].apply(lambda x: pd.Series(parse_duration(x)))

print("\nSample durations after parsing:")
print(df[['duration','duration_int','duration_unit']].head(10))
# Save the cleaned dataset
df.to_csv("netflix_titles_cleaned.csv", index=False)
print("\nCleaned dataset saved as 'netflix_titles_cleaned.csv'")

