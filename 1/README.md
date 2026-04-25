# Request Queue Simulator

A simple async Python program that simulates generating and processing requests using a FIFO queue.

## How it works

1. For each request in `constants.py`, the program schedules it to be added to the queue after `generate_delay` seconds.
2. It then waits `process_delay` seconds before processing the next request from the queue.
3. This repeats until all requests have been handled.

## Project structure

```
1/
├── main.py        # Entry point — runs the async loop
├── request.py     # Request and RequestQueue classes
├── constants.py   # Request data and config object
└── README.md
```

## Configuration

Edit the `config` object in `constants.py` to control timing:

```python
config = {
    "generate_delay": 1,   # seconds before a request is added to the queue
    "process_delay": 3,    # seconds to wait before processing the next request
}
```

## Running

```bash
python main.py
```

Requires Python 3.7+ (uses `asyncio.run`). No external packages needed.
