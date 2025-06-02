import json
import random
from datasets import load_dataset


dataset = load_dataset("euclaise/writingprompts")
all_prompts = [entry["prompt"] for entry in dataset["train"]]

short_prompts = [p for p in all_prompts if len(p.strip()) < 100]
random.shuffle(short_prompts)
selected_prompts = short_prompts[:50000]
prompt_dicts = [{"prompt": prompt} for prompt in selected_prompts]

with open("prompts.json", "w") as f:
    json.dump(prompt_dicts, f, indent=2)
