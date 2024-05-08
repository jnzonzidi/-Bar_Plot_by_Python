import matplotlib.pyplot as plt
import pandas as pd

# Read the Excel file into a DataFrame
data = pd.read_excel('C:/Users/Jean/Desktop/Files/SMS.xlsx')

# Extract data from DataFrame
x = data.iloc[:, 0].values  # Assuming the first column contains Date
y = data.iloc[:, 1].values  # Assuming the second column contains counts SMS data

plt.bar(x, y)
plt.title("SMS Inter Entrants")
plt.xlabel("formatted_date")
plt.ylabel("sequence_count")
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility

plt.savefig('C:/Users/Jean/Desktop/Files/population_barchart.png')
plt.show()
