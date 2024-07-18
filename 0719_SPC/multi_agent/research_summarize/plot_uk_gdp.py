import matplotlib.pyplot as plt

# UK GDP data for the past 5 years
years = [2017, 2018, 2019, 2020, 2021]
gdp = [2961.13, 2871.33, 2851.41, 2697.81, 3141.51]

# Create a line graph
plt.figure(figsize=(10, 5))
plt.plot(years, gdp, marker='o')

# Adding title and labels
plt.title('UK GDP Over the Past 5 Years')
plt.xlabel('Year')
plt.ylabel('GDP in Billion USD')
plt.grid(True)

# Save the plot as an image
plt.savefig('uk_gdp_past_5_years.png')
plt.show()