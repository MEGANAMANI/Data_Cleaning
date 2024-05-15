import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\Megana\pythonProject\Quality_analyst\data cleaned dataset.csv')

subset_df = df.head(100)

entity_names_column = 'Department/Independent Agency'  # Replace 'Company Name' with the actual column name containing entity names

# Example of cleaning and standardizing entity names
subset_df.loc[:, entity_names_column] = subset_df[entity_names_column].apply(lambda x: x.strip())
subset_df.loc[:, entity_names_column] = subset_df[entity_names_column].apply(lambda x: x.title())
# Add more cleaning and standardization steps as needed

print(subset_df[entity_names_column])

subset_df.to_csv('cleaned_subset.csv', index=False)