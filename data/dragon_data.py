############################
# generate dragon data
############################

import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic dragon data
n_dragons = 100
dragon_data = pd.DataFrame({
    'fire_power': np.random.normal(70, 15, n_dragons),
    'wing_span': np.random.normal(15, 4, n_dragons),
    'scale_thickness': np.random.normal(5, 2, n_dragons),
    'hoard_size': np.random.exponential(300, n_dragons),
    'age': np.random.randint(1, 500, n_dragons),
    'color': np.random.choice(['Red', 'Green', 'Blue', 'Black', 'White'], n_dragons),
    'region': np.random.choice(['North', 'South', 'East', 'West'], n_dragons)
})

dragon_data.head()

# Save the dataframe to a CSV file
file_path = "dragon_data.csv"
dragon_data.to_csv(file_path, index=False)
