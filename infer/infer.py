from vllm import LLM, SamplingParams
from tqdm import tqdm
import json
import argparse


def main(args):
  model_path = args.model_path
  model_name = args.model_name
  input_file = args.input_file
  output_file = args.output_file

  # input data
  with open(input_file, 'r') as f:
    data = json.load(f)
  prompts = []
  for key, value in tqdm(data.items(), desc="Processing", ncols=100):
    if "Qwen1.5" in model_name:
      prompt = "<|im_start|>user\n" + value['prompt'] + "\n<|im_start|>assistant\n"
      prompts.append(prompt)
    else:
      prompt = value['prompt']
      prompts.append(prompt)

  # llm inference 
  sampling_params = SamplingParams(temperature=0, top_p=0.95, top_k=-1, max_tokens=8192)
  llm = LLM(model=model_path, gpu_memory_utilization=0.5, tensor_parallel_size=1,trust_remote_code=True)
  outputs = llm.generate(prompts, sampling_params)

  # output data
  i  = 0
  for key, value in tqdm(data.items(), desc="Processing", ncols=100):
    data[key]['answer'] = outputs[i].outputs[0].text
    data[key]['acc'] = 0
    i += 1
  with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--model_path', type=str, default = None)
  parser.add_argument('--model_name', type=str, default = None)
  parser.add_argument('--input_file', type=str, default = None)
  parser.add_argument('--output_file', type=str, default = None)
  args = parser.parse_args()
  main(args)
