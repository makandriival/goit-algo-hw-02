config = {
    "generate_delay": 1,
    "process_delay": 5,
    "delay_between": 2,
    "requests_count": 10
}

requests = [{"id": i + 1, "email": f"user{i + 1}@example.com", "description": f"Request description {i + 1}"} for i in range(config["requests_count"])]
