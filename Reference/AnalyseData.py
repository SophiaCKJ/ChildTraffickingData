print("Welcome to AnalyseData.py")

# Step 1: Define the function to read the CSV file
def read_csv_file(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
        
    # Step 2: Split each line into a list of values (assuming comma-separated values)
    data = []
    for line in lines:
        # Strip leading/trailing whitespace and split by commas
        row = line.strip().split(',')
        data.append(row)
    
    return data

# Step 3: Process the loaded data
file_path = 'data_glotip.csv'  # Change this to the path of your CSV file
data = read_csv_file(file_path)

# Step 4: Display the first few rows to verify the data
print("Headers:", data[0])  # First row is usually the header
print("First Data Row:", data[1])  # Example of the first data row
print("Second Data Row:", data[2])  # Example of the second data row

# Step 5: Clean the data (remove metadata)
# Remove the first two rows (metadata) from the data variable
cleaned_data = data[2:]  # Skip the first two rows

# Display the cleaned data to verify
print("Headers:", cleaned_data[0])  # First row after cleaning should be the header
print("First Data Row:", cleaned_data[1])  # Example of the first actual data row

# Step 6: Filter the data for specific subregion
# Filter data for rows where the "Subregion" is "Western Europe"
filtered_data = []  # Initialize an empty list to store the results
for row in cleaned_data:
    if row[3] == "Western Europe":
        filtered_data.append(row)

# Display the filtered data to verify
print("Filtered Data (Headers):", cleaned_data[0])  # The headers
print("Number of Rows Matching 'Western Europe':", len(filtered_data))  # Total matching rows

# Optionally display a sample of the data
if filtered_data:
    print("First Matching Row:", filtered_data[0])
else:
    print("No matching rows found.")

# Step 7: Extract all the countries from the filtered data
countries_in_western_europe = []  # Initialize an empty list for countries
for row in filtered_data:
    countries_in_western_europe.append(row[1])  # Add the country name (column index 1)

# Display the unique list of countries
unique_countries = list(set(countries_in_western_europe))  # Remove duplicates
print("Countries in Western Europe:", unique_countries)
print("Number of Countries:", len(unique_countries))

# Step 8: Extract data based on multiple conditions that we define
# Further refine the data based on multiple conditions
refined_data = []  # Initialize an empty list for refined data
for row in filtered_data:
    if row[4] == "Detected trafficking victims" and row[6] == "Total" and row[7] == "Female":
        refined_data.append(row)

# Display the refined data to verify
print("Number of Rows Matching All Conditions:", len(refined_data))
if refined_data:
    print("Sample Row:", refined_data[0])  # Display the first row as a sample
else:
    print("No rows match the specified conditions.")

# Step 9: Group data by country
grouped_data = {}  # Dictionary to hold grouped data

for row in refined_data: # Iterate over the refined data
    country = row[1]  # Column index 1 contains the country name
    if country not in grouped_data:
        grouped_data[country] = []  # Initialize an empty list for this country
    grouped_data[country].append(row)  # Add the row to the corresponding country's list

# Display the grouped data for verification
for country, entries in grouped_data.items():
    print(f"Country: {country}, Number of Entries: {len(entries)}")
    print(f"Sample Entry for {country}: {entries[0]}")  # Display a sample row for each country

import matplotlib.pyplot as plt # Import the Matplotlib library for plotting
import numpy as np # Import the NumPy library for numerical operations

# Step 10: Create a list of results for a specific country (e.g., France)
# Extract data for France
france_data = grouped_data.get("France", [])  # Get the list of entries for France, default to an empty list

# Prepare data for plotting as lists
age_group = []
years = []
values = []

for row in france_data:
    try:
        if row[8] == 'Total': # Once we reach the total row, we can break
            break 
        age_group.append(row[8])  # Column index 5 is the "Age group"
        year = int(row[9])  # Column index 9 is the "Year"
        value = int(row[11])  # Column index 11 is the "txtValue"
        years.append(year) # Add the year to the list of years
        values.append(value) # Add the value to the list of values
    except ValueError:
        # Skip rows with invalid or non-integer data
        print(f"Skipping row with invalid data: {row}")

# Step 11: Error Checking to ensure data lists are of the same length
# Check the length of the lists and print error if not
if len(age_group) != len(years) or len(years) != len(values):
    print("Error: Data lists are not of the same length.")
else:
    print("Data lists are of the same length.")

# Step 12: Prepare the specific data for plotting
# Normalize age group names
normalized_age_group = ['18 years and over' if age == '18 years or over' else age for age in age_group]

# Prepare data for plotting
x_positions = np.arange(len(years) // 2)  # Half the size since there are two bars per year
bar_width = 0.4

# Split values into separate lists for each age group
under_17 = []
over_18 = []

for age, value in zip(normalized_age_group, values):
    if age == '0 to 17 years':
        under_17.append(value)
    elif age == '18 years and over':
        over_18.append(value)

# Ensure the x_positions align
year_labels = years[::2]  # Take one label per year (since two entries correspond to one year)

# Step 13: Plot the data for France
# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(x_positions, under_17, width=bar_width, label='0 to 17 years', color='skyblue')
plt.bar(x_positions + bar_width, over_18, width=bar_width, label='18 years and over', color='salmon')

# Add plot details
plt.title('Detected Trafficking Victims in France by Age Group')
plt.xlabel('Year')
plt.ylabel('Counts')
plt.xticks(x_positions + bar_width / 2, year_labels)  # Center x-ticks between grouped bars
plt.legend(title='Age Group')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print("End of AnalyseData.py")

# Questions to Improve this Code:

# 1. The data is stored as a csv file, could this be a problem for our values over 999?
# 2. In Step 10 we are breaking the loop when we reach the total row, is this the best approach?
# 3. We do a bar chart, how might we plot with a line or scatter chart instead?