import json
import re
from tqdm import tqdm
import os
import pandas as pd
import argparse



def judge_file(file_path):
	with open(file_path, 'r') as f:
		data = json.load(f)

	num = 0 
	acc = 0

	dict_acc = {}
	acc_count = {}
	for key, value in tqdm(data.items(), desc="Processing", ncols=100):
		answer = value['answer']
		correct = value["correct"]
		category = value["category"]
		
		
		if category not in dict_acc:
			dict_acc[category] = [0,1]
		if category in dict_acc:
			dict_acc[category][1] += 1
		
		
		match = re.search(r'\[\[([A-Z])\]\](?!(?:[^\[]*\[\[[A-Z]\]\])+[^\[]*\[\[\1\]\])', answer)
		num += 1
		if match:
			
			value['answer_select'] = match.group(1)
			choice = match.group().replace("[", "").replace("]", "")

			if choice == correct:
				value['acc'] = 1
				acc += 1
				dict_acc[category][0] += 1
			
		

	for key, value in dict_acc.items():
		acc_count[key] = value[0]
		dict_acc[key] = round(value[0] / value[1], 3)


	with open(file_path, 'w') as f:
		json.dump(data, f, indent=4,ensure_ascii=False)

	

	dict_acc['overall'] = round(acc / num,3)
	match1 = re.search(r'result_final/(.*?).json', file_path)

	print(match1.group(1))
	print(dict_acc)
	return match1.group(1),dict_acc,acc_count

def to_csv(folder_p, csv_p):
	folder_path = folder_p
	file_names = os.listdir(folder_path)
	file_paths = [os.path.join(folder_path, file_name) for file_name in file_names]
	file_paths = [path for path in file_paths if os.path.isfile(path)]

	
	table = {}
	data = []

	

	for path in file_paths:
		jf = judge_file(path)
		table[jf[0]] = jf[1]
		data.append(list(jf[1].values()))

		
	print(table)
	model_list = []
	category_list = []
	for k,v in table.items():
		model_list.append(k)
		category_list = list(v.keys())
	print(model_list)
	print(category_list)
	print(data)

	df = pd.DataFrame(data,columns=category_list,index=model_list)
	df.to_csv(csv_p)

def main(args):
	model_result_path = args.model_result_path
	folder_path = args.folder_path
	csv_path = args.csv_path
	
	judge_file(model_result_path)
	to_csv(folder_path, csv_path)




if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--model_result_path', type=str, default = None)
	parser.add_argument('--folder_path', type=str, default = None)
	parser.add_argument('--csv_path', type=str, default = None)
	
	args = parser.parse_args()
	main(args)

