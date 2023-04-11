import pandas as pd

# Load the Excel file
df = pd.read_excel(r"C:\Users\91848\Downloads\Daily water consumption (2).xlsx", index_col=0)

# Get the row names
row_names = df.index.tolist()

# Print the row names
print(row_names)


datetime.strptime(row['Date'], "%y-%m-%d").strftime("%Y-%m-%d %H:%M:%S"),
date=datetime.strptime(row['Date'].strftime('%Y-%m-%d %H:%M:%S')), 