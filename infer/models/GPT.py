from openai import OpenAI
import json
from tqdm import tqdm


API_KEY = ''
BASE_URL = ''
source_path = ''
save_path = ''

def score(source_path, save_path):

	client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

	def response_to_json(text):
		response = client.chat.completions.create(
			# model="gpt-4-turbo",  "gpt-3.5-turbo"
			model="gpt-4-turbo",
			messages=[
				{"role": "user",  "content": text}
			],
			stream=False, max_tokens=512, top_p=0.9, temperature=0.9)
		
		data_str = response.choices[0].message.content.strip()
		print(data_str)
		return data_str

	with open(source_path, 'r') as f:
		data = json.load(f)

	for key, value in tqdm(data.items(), desc="Processing", ncols=100):
		prompt = value['prompt']
		res = response_to_json(prompt)
		data[key]['answer'] = res
		print(data[key])
	

	with open(save_path, 'w') as f:
		json.dump(data, f, indent=4,ensure_ascii=False)
