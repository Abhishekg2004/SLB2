import pandas as pd

sales_data_1 = pd.DataFrame({
    'OrderID': [1, 2, 3, 4],
    'Product': ['Laptop', 'Tablet', 'Smartphone', 'Headphones'],
    'Sales': [1200, 800, 1500, 300]
})

sales_data_2 = pd.DataFrame({
    'OrderID': [3, 4, 5, 6],
    'Product': ['Smartphone', 'Headphones', 'Smartwatch', 'Tablet'],
    'Sales': [1500, 300, 200, 900]
})

print("Sales Data 1:\n", sales_data_1,"\nSales Data 2:\n", sales_data_2)

merged_data = pd.merge(sales_data_1, sales_data_2, on='OrderID', how='inner', )
print("\nMerged Data (Inner Join):\n", merged_data)

combined_data = pd.concat([sales_data_1, sales_data_2], ignore_index=True)
print("\nCombined Data (Concatenated Vertically):\n", combined_data)

reshaping_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar'],
    'Product_A': [100, 150, 130],
    'Product_B': [90, 80, 120]
})
print("\nReshaping Data (Original):\n", reshaping_data)

melted_data = pd.melt(reshaping_data, id_vars='Month', var_name='Product', value_name='Sales')
print("\nMelted Data (Long Format):\n", melted_data)

pivoted_data = melted_data.pivot(index='Month', columns='Product', values='Sales')
print("\nPivoted Data (Wide Format):\n", pivoted_data)