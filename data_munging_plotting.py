import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the path to the Auto.csv file
data_folder = "data"
file_name = "Auto.csv"
file_path = os.path.join(data_folder, file_name)

# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: File '{file_name}' not found in the '{data_folder}' folder.")
else:
    # Step 1: Load the data
    print("Loading data...")
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
    print("First 5 rows of the dataset:")
    print(data.head())

    # Step 2: Data munging (cleaning and processing)
    print("\nCleaning and processing data...")
    # Convert columns to appropriate data types if necessary
    data['mpg'] = pd.to_numeric(data['mpg'], errors='coerce')
    data['horsepower'] = pd.to_numeric(data['horsepower'], errors='coerce')

    # Drop rows with missing or invalid values
    data = data.dropna()
    print("Data after cleaning:")
    print(data.head())

    # Step 3: Data filtering
    print("\nFiltering data...")
    # Example: Filter rows where horsepower is greater than 100
    filtered_data = data[data['horsepower'] > 100]
    print(f"Filtered data (horsepower > 100):")
    print(filtered_data.head())

    # Step 4: Plotting
    print("\nPlotting data...")
    plt.figure(figsize=(10, 6))
    plt.scatter(filtered_data['horsepower'], filtered_data['mpg'], color='blue', alpha=0.7)
    plt.title("Horsepower vs MPG")
    plt.xlabel("Horsepower")
    plt.ylabel("MPG")
    plt.grid(True)
    plt.show()
