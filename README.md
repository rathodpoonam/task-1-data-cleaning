# 🧹 Task 1: Data Cleaning - Customer Personality Analysis

## 📁 Dataset
- **Source**: [Kaggle - Customer Personality Analysis]
- **File Used**: `marketing_campaign.csv`

## 🛠️ Tools Used
- Python
- Pandas
- Datetime module

## 🧼 Data Cleaning Steps
1. Loaded the dataset using tab (`\t`) separator.
2. Dropped rows with missing values and removed duplicate entries.
3. Renamed all column headers to lowercase with underscores for consistency.
4. Standardized categorical text fields: `education`, `marital_status`.
5. Converted the `dt_customer` column to datetime format.
6. Created a new `age` column based on `year_birth`.
7. Corrected data types for numeric fields: `income`, `kidhome`, `teenhome`.
8. Exported the cleaned data to a new file: `cleaned_customer_data.csv`.

## ✅ Output
- Cleaned and structured dataset ready for further analysis or modeling.
- Format and types now consistent, and unnecessary or dirty data removed.
