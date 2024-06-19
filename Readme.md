## Introduction
**GIE-Bench** 

We introduce GIEBench, a comprehensive benchmark that includes 11 identity dimensions, covering 97 group identities with a total of 999 single-choice questions related to specific group identities. GIEBench is designed to evaluate the empathy of LLMs when presented with specific group identities such as gender, age, occupation, and race, emphasizing their ability to respond from the standpoint of the identified group. The detailed statistical information can be found in the image below.
<div style="text-align: center;">
  <img src="item.png" width="80%">
</div>
Initially, a collection of controversial topics is developed using web resources, manual selection, and GPT-4, each corresponding to a specific identity. Subsequently, we annotate attitude labels from the perspectives of these identities. We also utilize GPT-4 to generate four responses for each topic, ensuring that only one response aligns with the identity's stance. Finally, using the established identities, topics, and responses, we design three types of prompts to LLMs in selecting the most appropriate response. In the COT-Prompt, a Chain of Thought (COT) is provided along with identity information. In the ID-Prompt, only the identity is disclosed, while the Raw-Prompt includes no additional information.The detailed process can be found in the image below.
<div style="text-align: center;">
  <img src="pipline.png" width="80%">
</div>
## Example


We analyze the extent to which LLMs understand the standpoint of the given identity by comparing the difference in accuracy between CoT-Prompt and Raw-Prompt.

<div style="text-align: center;">
  <img src="Raw2COT.png" width="80%">
</div>

We analyze the empathy of LLMs towards the given identity standpoint by comparing the difference in accuracy between ID-Prompt and Raw-Prompt.
<div style="text-align: center;">
  <img src="Raw2ID.png" width="80%">
</div>

The results revealed that although certain LLMs can largely understand the user's identity standpoint, they do not spontaneously exhibit empathy when not explicitly instructed to consider the user's perspective. This highlights the shortcomings of current alignment techniques.

  
## Installation
```python
pip install -r requirements.txt
```


## Inference
You can directly perform inference on `` model to be tested using the following command:
```python
python infer/infer.py --model_name yi-vl-6b-chat --mode none --output_dir ./results
```

`--mode`: We provide various evaluation modes, including no additional prompts (none), keyword-based prompts (domain, emotion, rhetoric), chain-of-thought prompts (cot), and few-shot prompts (1-shot, 2-shot, 3-shot). You can use the mode parameter to select which evaluation modes to use, with the option to choose multiple modes. By default, all modes will be evaluated in a loop.

`--infer_limit`: The input for this parameter is an integer, used to limit the number of problems for this inference, aimed at saving costs while debugging API, default is unlimited.

During inference, a temporary file .jsonl.tmp will be saved. If the inference is unexpectedly interrupted, you can directly rerun the command to resume inference from the breakpoint.

After inference is complete, you can check the response field in the saved JSONL file in `output_dir`. Normally, this field should be of string type; if it is of dict type, the error field will contain error information. Rerunning the command can directly re-infer the issues that caused errors.

### Run Custom Model
`--model_name` needs to align with the filenames in the `infer/models` directory. We have some built-in models available for direct selection. 

If you add a `custom model` to be tested, you need to refer to the files in the `infer/models` directory to add a new `.py` file and add your config in [\_\_init\_\_.py](infer/models/__init__.py).


## Evaluation

After you finish inference and confirm there are no error messages, please run the answer parsing and evaluation pipeline as follows: 
```
python eval.py --model_name yi-vl-6b-chat --mode none --output_dir ./results --save_dir ./results_with_status
```
Detailed evaluation results can be found in the `save_dir`.

Alternatively, you can use the following command to evaluate the inference results of all models:
```
python eval.py --evaluate_all --output_dir ./results --save_dir ./results_with_status
```
## Citation

**BibTeX:**



```
