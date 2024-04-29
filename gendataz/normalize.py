import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load the CSV file. Assume there are no headers and it's comma-separated.
df = pd.read_csv('extracted_data.csv', header=None)

# Assuming the second column (index 1) needs to be transformed and normalized
values = df.iloc[:, 1].values.reshape(-1, 1)

# Apply log transformation: log(1 + x) to handle zero values safely
log_transformed_values = np.log1p(values)

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Normalize the log-transformed values
normalized_values = scaler.fit_transform(log_transformed_values)

# Replace the original values with the normalized ones in the dataframe
df.iloc[:, 1] = normalized_values.flatten()

# Write the modified dataframe to a new CSV file, without the index
df.to_csv('extracted_data_norm.csv', index=False, header=False)
