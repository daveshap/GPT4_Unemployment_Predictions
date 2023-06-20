import os
import yaml
import pandas as pd

# Initialize an empty list to store the data
data = []

# Loop through every file in the directory
for filename in os.listdir('jobs/'):
    if filename.endswith('.yaml'):
        with open(os.path.join('jobs/', filename), 'r') as file:
            # Load the YAML data
            yaml_data = yaml.safe_load(file)

            # Convert the TOT_EMP field to a float
            yaml_data['TOT_EMP'] = float(yaml_data['TOT_EMP'].replace(',', ''))

            # Add the data to the list
            data.append(yaml_data)

# Convert the list to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)