import matplotlib.pyplot as plt

# Data
years = [2017, 2018, 2019, 2020, 2021]
gdp = [2939.59, 2871.34, 2851.41, 2697.81, 3141.51]

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(years, gdp, marker='o', linestyle='-', color='b')

# Add a title and labels
plt.title('UK GDP Over the Past 5 Years')
plt.xlabel('Year')
plt.ylabel('GDP in Billions (USD)')
plt.grid(True)

# Save the plot as an image file
plt.savefig('uk_gdp_past_5_years.png')

# Show the plot
plt.show()