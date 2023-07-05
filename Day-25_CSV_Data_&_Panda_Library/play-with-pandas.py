import pandas as pd
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
        "Nationality": ['Briton', 'Briton', 'Irish']
    }
)

# Nationality = pd.Series(['Briton', 'Briton', 'Irish'])

print(df)
print(max(df['Age']))
print(df['Age'].min())
print(df.describe())
