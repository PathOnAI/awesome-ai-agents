import matplotlib.pyplot as plt

# Data for UK's GDP over the last 5 years
years = [2018, 2019, 2020, 2021, 2022]
gdp = [2.86, 2.83, 2.71, 3.13, 3.19]

plt.figure(figsize=(10, 6))
plt.plot(years, gdp, marker='o')
plt.title('UK GDP Over the Past 5 Years')
plt.xlabel('Year')
plt.ylabel('GDP in USD (Trillions)')
plt.grid(True)
plt.savefig('UK_GDP_Plot.png')
plt.show()