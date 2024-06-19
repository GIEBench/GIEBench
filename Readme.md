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

Here are a example:

<div style="text-align: center;">
  <img src="COT-Prompt.png" width="50%">
  <img src="ID-Prompt.png" width="50%">
  <img src="Raw-Prompt.png" width="50%">
</div>

We analyze the extent to which LLMs understand the standpoint of the given identity by comparing the difference in accuracy between CoT-Prompt and Raw-Prompt.

<div style="text-align: center;">
  <img src="Raw2COT.png" width="50%">
</div>

We analyze the empathy of LLMs towards the given identity standpoint by comparing the difference in accuracy between ID-Prompt and Raw-Prompt.
<div style="text-align: center;">
  <img src="Raw2ID.png" width="50%">
</div>

The results revealed that although certain LLMs can largely understand the user's identity standpoint, they do not spontaneously exhibit empathy when not explicitly instructed to consider the user's perspective. This highlights the shortcomings of current alignment techniques.
## Contact
- Leyan Wang: Wleyan@bupt.edu.cn
- Ge Zhang: gezhang@umich.edu
  


```
