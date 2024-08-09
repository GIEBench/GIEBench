import argparse
import json
from tqdm import tqdm
from vllm import LLM, SamplingParams

def load_prompts(prompt_path):
    """Load prompts from a JSON file."""
    with open(prompt_path, 'r') as f:
        data = json.load(f)
    return data

def save_results(data, model_result_path):
    """Save generated results to a JSON file."""
    with open(model_result_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def generate_responses(llm, prompts):
    """Generate responses using the provided LLM and prompts."""
    sampling_params = SamplingParams(temperature=0, top_p=0.95, top_k=-1, max_tokens=8192)
    return llm.generate(prompts, sampling_params)

def main(args):
    # Load input data
    data = load_prompts(args.prompt_path)
    prompts = [value['prompt'] for value in data.values()]

    # Setup LLM
    llm = LLM(model=args.model_path, gpu_memory_utilization=0.5,
              tensor_parallel_size=1, trust_remote_code=True)

    # Generate responses
    outputs = generate_responses(llm, prompts)

    # Update data with generated responses
    for (key, output), value in zip(data.items(), outputs):
        value['answer'] = output.outputs[0].text
        value['acc'] = 0  # assuming 'acc' needs to be reset or calculated

    # Save the results
    save_results(data, args.model_result_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate responses using an LLM model.")
    parser.add_argument('--model_path', type=str, required=True, help="Path to the LLM model.")
    parser.add_argument('--prompt_path', type=str, required=True, help="Path to the input JSON file with prompts.")
    parser.add_argument('--model_result_path', type=str, required=True, help="Path to save the generated results.")
    args = parser.parse_args()
    main(args)

