
import pandas as pd

files = {
    "League Table": "premier_league.csv",
    "Top Scorers": "top_scorers.csv"
}

for title, filename in files.items():
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)

    data = pd.read_csv(filename)

    print("Rows:", len(data))
    print("Columns:", data.columns.tolist())
    print("Missing values:", data.isnull().sum().sum())
    print("Duplicate rows:", data.duplicated().sum())

    print("\nFirst 5 rows:")
    print(data.head().to_string(index=False))

    print("\nData types:")
    print(data.dtypes)
