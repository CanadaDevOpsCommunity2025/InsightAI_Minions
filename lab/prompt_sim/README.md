
### 1. Install Dependencies

```bash
pip install datasets locust
```

### 2. Prepare the Prompt Dataset (Optinal)

Run the following script to generate `prompts.json` containing 50,000 prompts under 100 characters:

```bash
python dataset_prep.py
```

### 3. Run the Load Test

Execute the load test using Locust in headless mode:

```bash
locust -f main.py --headless \
       -u 10 -r 10 \
       --host <target host> \
       --run-time 2m
```

**Parameters Explained:**

- `--headless`: Runs Locust without the web UI.
- `-u 10`: Simulates 10 concurrent users.
- `-r 10`: Spawns 10 users per second.
- `--host`: Target host URL of the vLLM server.
- `--run-time 2m`: Runs the test for 2 minutes.
