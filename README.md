# -Bar_Plot_by_Python

This script performs the following tasks:

Imports Libraries:
matplotlib.pyplot is imported as plt to create plots.
pandas is imported as pd to handle data, particularly reading Excel files.
Reads Excel File:
It reads an Excel file named 'SMS.xlsx' located at the specified path into a DataFrame using pd.read_excel() function. This function reads the data from the Excel file and converts it into a DataFrame, which is a tabular data structure.
Extracts Data from DataFrame:
It extracts data from the DataFrame:
The variable x is assigned the values of the first column of the DataFrame, assuming it contains dates.
The variable y is assigned the values of the second column of the DataFrame, assuming it contains counts of SMS data.
Creates a Bar Plot:
It creates a bar plot using plt.bar() function, where x represents the x-axis values (dates) and y represents the y-axis values (SMS counts).
Sets Plot Title and Labels:
It sets the title of the plot using plt.title().
It sets the labels for x-axis and y-axis using plt.xlabel() and plt.ylabel() respectively.
Customizes x-axis Ticks:
It rotates the x-axis labels by 45 degrees for better visibility using plt.xticks(rotation=45).
Saves the Plot as an Image:
It saves the generated plot as an image file named 'population_barchart.png' at the specified path using plt.savefig().
Displays the Plot:
It displays the plot using plt.show(). This function shows the plot in a pop-up window.
Overall, this script reads data from an Excel file, creates a bar plot based on the data, customizes the plot appearance, saves the plot as an image file, and finally displays the plot.
