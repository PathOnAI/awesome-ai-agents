import matplotlib.pyplot as plt

years = ['2017', '2018', '2019', '2020', '2021']
gdp = [2809.47, 2871.09, 2851.41, 2697.81, 3141.51]

plt.figure(figsize=(10, 6))
plt.plot(years, gdp, marker='o')
plt.title('UK GDP Over the Past 5 Years')
plt.xlabel('Year')
plt.ylabel('GDP in Billion USD')
plt.grid(True)
plt.savefig('uk_gdp_chart.png')
plt.show()