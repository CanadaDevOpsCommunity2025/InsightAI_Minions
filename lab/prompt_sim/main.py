import json
import random
from locust import HttpUser, task, between

# Load prompts from the JSON file
with open("prompts.json", "r") as f:
    prompt_data = json.load(f)
    PROMPTS = [entry["prompt"] for entry in prompt_data]

class ChatCompletionUser(HttpUser):
    wait_time = between(1, 3)  # Think-time between requests (seconds)

    @task
    def completion(self):
        payload = {
            "model": "gpt2",
            "prompt": random.choice(PROMPTS),
            "max_tokens": 50
        }
        self.client.post("/v1/completions", json=payload)

