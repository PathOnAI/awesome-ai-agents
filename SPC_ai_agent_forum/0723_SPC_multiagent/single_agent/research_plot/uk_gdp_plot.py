import matplotlib.pyplot as plt

# Data
years = [2017, 2018, 2019, 2020, 2021]
gdp = [2856, 2871, 2851.41, 2697.81, 3141.51]

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(years, gdp, marker='o', linestyle='-', color='b')
plt.title('UK GDP Over the Past 5 Years')
plt.xlabel('Year')
plt.ylabel('GDP in Billion USD')
plt.grid(True)
plt.savefig('uk_gdp_over_past_5_years.png')
plt.show()