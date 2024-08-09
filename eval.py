import json
import re
from tqdm import tqdm
import os
import pandas as pd
import argparse

def load_data(file_path):
    """
    Load JSON data from a file.
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def write_data(file_path, data):
    """
    Write JSON data to a file.
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

def analyze_data(data):
    """
    Analyze data and compute accuracy statistics.
    """
    num = 0 
    acc = 0
    dict_acc = {}
    for key, value in tqdm(data.items(), desc="Processing", ncols=100):
        answer = value['answer']
        correct = value["correct"]
        category = value["category"]
        
        if category not in dict_acc:
            dict_acc[category] = [0, 1]
        else:
            dict_acc[category][1] += 1
        
        match = re.search(r'\[\[([A-Z])\]\](?!(?:[^\[]*\[\[[A-Z]\]\])+[^\[]*\[\[\1\]\])', answer)
        num += 1
        if match:
            choice = match.group(1)
            value['answer_select'] = choice
            if choice == correct:
                value['acc'] = 1
                acc += 1
                dict_acc[category][0] += 1
    
    for key, value in dict_acc.items():
        dict_acc[key] = round(value[0] / value[1], 3)
    dict_acc['overall'] = round(acc / num, 3)
    return dict_acc

def process_file(file_path):
    """
    Process a single JSON file to compute accuracy and update the file.
    """
    data = load_data(file_path)
    if data:
        dict_acc = analyze_data(data)
        write_data(file_path, data)
        return file_path, dict_acc

def generate_csv(folder_path, csv_path):
    """
    Process all JSON files in a folder and generate a CSV with accuracy data.
    """
    file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.json')]
    data = [process_file(path) for path in file_paths if os.path.isfile(path)]
    data = [d for d in data if d is not None]
    
    df = pd.DataFrame.from_records([dict_acc for _, dict_acc in data], index=[os.path.basename(path) for path, _ in data])
    df.to_csv(csv_path)

def main(args):
    """
    Main function to process results and generate CSV.
    """
    if args.model_result_path:
        process_file(args.model_result_path)
    if args.folder_path and args.csv_path:
        generate_csv(args.folder_path, args.csv_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_result_path', type=str, help="Path to a single JSON file with model results")
    parser.add_argument('--folder_path', type=str, help="Path to folder containing JSON files")
    parser.add_argument('--csv_path', type=str, help="Path to output CSV file")
    args = parser.parse_args()
    main(args)


