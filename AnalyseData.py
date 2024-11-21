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