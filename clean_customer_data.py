import pandas as pd

df = pd.read_csv("marketing_campaign.csv", sep='\t')

print("Initial shape:", df.shape)
print("Missing values:\n", df.isnull().sum())

df = df.dropna()


df = df.drop_duplicates()


df.columns = df.columns.str.lower().str.replace(" ", "_")

df['dt_customer'] = pd.to_datetime(df['dt_customer'], errors='coerce')

df['education'] = df['education'].str.lower().str.strip()


df['marital_status'] = df['marital_status'].str.lower().str.strip()
df['marital_status'] = df['marital_status'].replace({
    'together': 'married',
    'divorced': 'separated',
    'widow': 'separated',
    'alone': 'single',
    'absurd': 'single',
    'yo-lo': 'single'
})


df['income'] = df['income'].astype(int)
df['kidhome'] = df['kidhome'].astype(int)
df['teenhome'] = df['teenhome'].astype(int)
df['age'] = 2025 - df['year_birth'] 


print("\nCleaned shape:", df.shape)
print("\nCleaned sample:\n", df.head())

df.to_csv("cleaned_customer_data.csv", index=False)