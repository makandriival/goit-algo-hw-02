from threading import Timer
import asyncio
from request import RequestQueue
from constants import requests, config

rq = RequestQueue()
processed_count = 0

def generate(id, email, description):
    print(f"generating request {id}...")
    rq.generate_request(id, email, description)
    print(f"Queue size: {rq.get_queue_size()}")
    
def process(id):
    if rq.get_queue_size() > 0:
        print(f"processing request {id}...")
        rq.process_request()
        print(f"Queue size: {rq.get_queue_size()}")
    
async def req_loop():
    for r in requests:
        Timer(config["generate_delay"], generate, args=(r["id"], r["email"], r["description"])).start()
        await asyncio.sleep(config["delay_between"])

async def processing_loop():
    global processed_count
    
    while True:
        print("Checking for requests to process...")
        
        if rq.get_queue_size() > 0:
            process(rq.queue.queue[0].id)
            processed_count += 1
        await asyncio.sleep(config["process_delay"])
        
        print(f"Processed {processed_count} requests so far.") 
        if processed_count >= config["requests_count"]:
            print("All requests processed.")
            break

async def main():
    await asyncio.gather(req_loop(), processing_loop())

asyncio.run(main())
