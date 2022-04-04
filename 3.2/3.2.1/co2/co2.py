import matplotlib.pyplot as plt
import pandas as pd
import math

# Read csv data as pandas data frame
co2_data = pd.read_csv("co2_data.csv", header=0)

# Debug print statement (step 40)
print(co2_data)

# Set unrecorded values to NaN (not a number)
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)

# Debug print statement (step 40)
print(co2_data)

# Filter out NaN
co2_data.dropna(subset=['Average'], inplace=True)

# Debug print statement (step 40)
print(co2_data)

# Plot the data
plt.plot(co2_data['Year'], co2_data['Average'], color='gray')
plt.ylabel('CO2 Levels in PPM')
plt.xlabel('Year')
plt.title('Change in CO2 Levels')

# Display the plot
plt.show()