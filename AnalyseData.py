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

print(data[30000])