from transformers import pipeline

import os
os.environ['SSL_CERT_FILE'] = 'path/to/certificate.pem'


def standardize_entity_name_llm(entity_name):
    model_name = "EleutherAI/gpt-neo-125M"  # You can choose a different LLM model if needed
    nlp = pipeline("text-generation", model=model_name, tokenizer=model_name)
    standardized_name = nlp(entity_name, max_length=50, max_new_tokens=50, do_sample=False, truncation=True)[0]['generated_text'].strip()
    return standardized_name


# Example usage
entity_name = "Department/Independent Agency"
standardized_name = standardize_entity_name_llm(entity_name)
print("Standardized name:", standardized_name)


import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\Megana\pythonProject\Quality_analyst\data cleaned dataset.csv')

# Select entity names column
entity_names_column = 'Department/Independent Agency'  # Replace with actual column name

# Apply standardization function to each entity name
df[entity_names_column] = df[entity_names_column].apply(standardize_entity_name_llm)


subset_df = df.head(100)  # Select first 100 records as subset
subset_df[entity_names_column] = subset_df[entity_names_column].apply(standardize_entity_name_llm)
print(subset_df[entity_names_column])
