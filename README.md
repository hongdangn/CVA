# CVA: Cross-Vocabulary Alignment for Vision-Language Embedding
Models
## Clone repo
```
git clone https://github.com/hongdangn/CVA.git
```
## Set up env
```bash
cd CVA
apt-get update
apt-get upgrade -y
apt install tmux zip unzip -y
apt-get install -y libgl1 libglib2.0-0
python -m venv vlm 
source vlm/bin/activate
```
## Dependencies
For installing dependencies, run the following commands:
```
1. pip install -r requirements.txt
2. python fix_lib.py
```
## Code Comment
If the errors still exist, please go to the image_processing_qwen2_vl.py and COMMENT these lines of code:
```
if size is not None and ("shortest_edge" not in size or "longest_edge" not in size):
    raise ValueError("size must contain 'shortest_edge' and 'longest_edge' keys.")
else:
    size = {"shortest_edge": 56 * 56, "longest_edge": 28 * 28 * 1280}
```
## Download dataset 
Download train/eval dataset/images here:
```bash
Train data: https://huggingface.co/datasets/TIGER-Lab/MMEB-train]
Evaluation data: https://huggingface.co/datasets/TIGER-Lab/MMEB-eval
```
## Acknowledgement
- We have adapted code from [VLM2Vec]([https://github.com/TIGER-AI-Lab/VLM2Vec]) and [B3](https://github.com/raghavlite/B3)
