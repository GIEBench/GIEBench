## Introduction
**GIE-Bench** 

We introduce GIEBench, a comprehensive benchmark that includes 11 identity dimensions, covering 97 group identities with a total of 999 single-choice questions related to specific group identities. GIEBench is designed to evaluate the empathy of LLMs when presented with specific group identities such as gender, age, occupation, and race, emphasizing their ability to respond from the standpoint of the identified group. The detailed statistical information can be found in the image below.
<div style="text-align: center;">
  <img src="img/item.png" width="80%">
</div>
Initially, a collection of controversial topics is developed using web resources, manual selection, and GPT-4, each corresponding to a specific identity. Subsequently, we annotate attitude labels from the perspectives of these identities. We also utilize GPT-4 to generate four responses for each topic, ensuring that only one response aligns with the identity's stance. Finally, using the established identities, topics, and responses, we design three types of prompts to LLMs in selecting the most appropriate response. In the COT-Prompt, a Chain of Thought (COT) is provided along with identity information. In the ID-Prompt, only the identity is disclosed, while the Raw-Prompt includes no additional information.The detailed process can be found in the image below.
<div style="text-align: center;">
  <img src="img/pipline.png" width="100%">
</div>



We analyze the extent to which LLMs understand the standpoint of the given identity by comparing the difference in accuracy between CoT-Prompt and Raw-Prompt.

<div style="text-align: center;">
  <img src="img/Raw2COT.png" width="100%">
</div>

We analyze the empathy of LLMs towards the given identity standpoint by comparing the difference in accuracy between ID-Prompt and Raw-Prompt.
<div style="text-align: center;">
  <img src="img/Raw2ID.png" width="100%">
</div>

The results revealed that although certain LLMs can largely understand the user's identity standpoint, they do not spontaneously exhibit empathy when not explicitly instructed to consider the user's perspective. This highlights the shortcomings of current alignment techniques.

  
## Installation
```python
pip install -r requirements.txt
```
## Download
First, download our data in the `data` folder, `YOUR_PROMPT_PATH` stands for your data path.
## Inference
You can perform inference on Your model to be tested using the following command:
```python
python infer/infer.py --model_path YOUR_MODEL_PATH --prompt_path YOUR_PROMPT_PATH --model_result_path YOUR_MODEL_RESULT_PATH
```

`--model_path`: This parameter indicates the path where your model is saved.

`--prompt_path`: This parameter indicates the path where your Prompt file is saved.

If your model requires an api to be called, use the following command:

```python
python infer/api_infer.py --prompt_path YOUR_PROMPT_PATH --model_result_path YOUR_MODEL_RESULT_PATH
```

After inference is complete, you can check the response field in the saved JSON file in `model_result_path`. 


## Evaluation

After you finish inference and confirm there are no error messages, please run the answer parsing and evaluation pipeline as follows: 
```
python eval.py --model_result_path YOUR_MODEL_RESULT_PATH --folder_path YOUR_RESULT_FOLDER_PATH --csv_path YOUR_CSV_PATH
```
`--folder_path`: This parameter indicates the path to your model's results folder.

`--csv_path`: This parameter indicates the path to the csv file that holds all your model score results.
Finally, the csv file records the correctness of your model with the Prompt you chose.
## Citation

**BibTeX:**



```
