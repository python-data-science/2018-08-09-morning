import pandas as pd

df = pd.read_csv('OfficeSupplies.csv')

# Add a new column called Total Price = Units * Unit Prince_Fielder
df['Total Price'] = df['Units'] * df['Unit Price']

# Show the mean and the sum for each rep per region
df.groupby(['Region','Rep'])['Total Price'].agg(['mean','sum'])

# Show totals by region
regions = df.groupby(['Region'])['Total Price'].agg(['sum']).reset_index()

# Show reps per region
reps = df.groupby(['Region'])['Rep'].unique().to_frame().reset_index()

# Using 'concat' to join the series and dataframe
merged = reps.merge(regions, on='Region').set_index('Region')

# Create a new column containing the count of reps per region
merged['count'] = merged.apply(lambda row: len(row['Rep']), axis=1)

# Create a new colum for normalized
merged['normalized'] = merged['sum'] / merged['count']
