print('Welcome to Analyse Data!')

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        row = line.strip().split(',')
        data.append(row)
    return data

file_path = 'data_glotip.csv'
data = read_csv_file(file_path)

print("Headers:", data[0])
print("First Data Row:", data[1])
print("Second Data Row:", data[2])

cleaned_data = data[2:]
print("Headers:", cleaned_data[0])
print("First Data Row:", cleaned_data[1])

filtered_data = []
for row in cleaned_data:
    if row[3] == "Western Europe":
        filtered_data.append(row)

print("Number of Rows Matching 'Western Europe':", len(filtered_data))

if filtered_data:
    print("First Matching Row:", filtered_data[0])
else:
    print("No matching rows found.")