
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

#### Option A: Headless Mode (Command-Line)

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

#### Option B: Web Interface Mode

To run the load test using Locust's web interface:

1. Start Locust without the `--headless` flag:

   ```bash
   locust -f main.py
   ```

2. Open your web browser and navigate to [http://localhost:8089](http://localhost:8089).

3. Fill in the following fields:

   - **Number of users to simulate**: e.g., `10`
   - **Spawn rate**: e.g., `10`
   - **Host**: e.g., `http://localhost:8000`

4. Click the **Start swarming** button to initiate the load test.

