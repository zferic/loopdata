import pandas as pd
from sklearn.model_selection import train_test_split
import os

def split_data_into_train_test(csv_file_path, output_folder, test_size=0.2, n_iterations=10):
    # Load the data
    data = pd.read_csv(csv_file_path)
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Create train/test splits for the specified number of iterations
    for iteration in range(1, n_iterations + 1):
        train_data, test_data = train_test_split(data, test_size=test_size, random_state=iteration)
        
        train_file_path = os.path.join(output_folder, f'extracted_data_norm_train_fold_{iteration}.csv')
        test_file_path = os.path.join(output_folder, f'extracted_data_norm_test_fold_{iteration}.csv')
        
        train_data.to_csv(train_file_path, index=False)
        test_data.to_csv(test_file_path, index=False)
        
        print(f"Iteration {iteration}: Train and test splits have been saved to {train_file_path} and {test_file_path}, respectively.")

# Usage
csv_file_path = '/media/zman/extrahd/gematria/data/gendataz/extracted_data_norm.csv'  # Update this path
output_folder = '/media/zman/extrahd/gematria/data/gendataz/foldsdata'  # Update this path
split_data_into_train_test(csv_file_path, output_folder, test_size=0.2, n_iterations=10)
