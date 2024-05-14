import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

file_path = "1_Data.csv" 
df = pd.read_csv(file_path) 

# Filter non-numerical columns
numerical_columns = df.select_dtypes(include=['number']).columns

# Select only numerical columns
numerical_df = df[numerical_columns]

# Plot heatmap using numerical DataFrame
sns.heatmap(numerical_df, annot=True, fmt=".1f", cmap="YlGnBu")  # Pass numerical_df instead of df

plt.show()

#print(df.describe())
