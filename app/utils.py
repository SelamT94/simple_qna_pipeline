import json

def load_data(data_path):
    with open(data_path, 'r') as file:
        data = json.load(file)
    return data

def save_data(data, output_path):
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)
