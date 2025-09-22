# Task 1: Data Cleaning and Preprocessing

## Objective
Clean and prepare the raw Netflix dataset for analysis.

## Tools
- Python 3
- Pandas

## Dataset
- Source: Netflix Movies and TV Shows (Kaggle)
- File: `netflix_titles.csv`

## Steps Performed
1. Loaded dataset into Pandas.
2. Checked for missing values using `.isnull()`.
3. Removed duplicate rows using `.drop_duplicates()`.
4. Standardized column names (lowercase, underscores, no special characters).
5. Trimmed whitespace in text columns.
6. Filled missing values:
   - `director`, `cast`, `country` → `"Unknown"`
   - `rating` → `"Not Rated"`
7. Converted `date_added` to datetime format.
8. Parsed `duration` into numeric `duration_int` and unit `duration_unit`.
9. Saved cleaned dataset as `netflix_titles_cleaned.csv`.

## Outcome
- Cleaned dataset ready for analysis.
- Columns are standardized and missing values handled.
- Duration is split into numbers and units for easier analysis.
