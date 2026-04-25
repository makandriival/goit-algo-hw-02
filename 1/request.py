from queue import Queue

class Request:
    def __init__(self, id, email, description):
        self.id = id
        self.email = email
        self.description = description

class RequestQueue:
    def __init__(self):
        self.queue = Queue()

    def generate_request(self, id, email, description):
        request = Request(id, email, description)
        self.queue.put(request)

    def process_request(self):
        if not self.queue.empty():
            request = self.queue.get()
            print(f"Processing request {request.id} from {request.email}: {request.description}")
        else:
            print("The queue is empty.")
    
    def get_queue_size(self):
        return self.queue.qsize()
