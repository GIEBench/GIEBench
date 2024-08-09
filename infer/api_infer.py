import argparse
import json
from openai import OpenAI
from tqdm import tqdm

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

def create_client(api_key, base_url):
    return OpenAI(base_url=base_url, api_key=api_key)

def get_response(client, text, params):
    try:
        response = client.chat.completions.create(
            model=params.get("model"),
            messages=[{"role": "user", "content": text}],
            stream=False, 
            max_tokens=params.get("max_tokens", 512),
            top_p=params.get("top_p", 0.9),
            temperature=params.get("temperature", 0.9)
        )
        data_str = response.choices[0].message.content.strip()
        return data_str
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

def process_prompts(client, source_path, save_path, model_params):
    try:
        with open(source_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("The source file was not found.")
        return

    for key, value in tqdm(data.items(), desc="Processing", ncols=100):
        prompt = value['prompt']
        res = get_response(client, prompt, model_params)
        if res is not None:
            data[key]['answer'] = res

    try:
        with open(save_path, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except IOError:
        print("Error saving the results.")

def main(args):
    config = load_config(args.config_path)
    client = create_client(config['api_key'], config['base_url'])
    model_params = config.get("model_params", {})
    model_params['model'] = args.model  # Use the model specified by the user
    process_prompts(client, args.prompt_path, args.model_result_path, model_params)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, required=True, help="Path to configuration JSON file")
    parser.add_argument('--model', type=str, required=True, help="Language model to use (e.g., 'gpt-4-turbo')")
    parser.add_argument('--prompt_path', type=str, required=True, help="Path to the input JSON file with prompts")
    parser.add_argument('--model_result_path', type=str, required=True, help="Path to save the JSON file with results")
    args = parser.parse_args()
    main(args)

