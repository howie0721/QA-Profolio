"""
Stress Test - Find System Breaking Point

This test pushes the system to its limits to find the breaking point.

Test Strategy:
1. Ramp up users quickly
2. Maintain high load
3. Observe when system starts failing

Metrics to watch:
- Response time increase
- Failure rate increase
- System resource usage (CPU, Memory)
"""

from locust import HttpUser, task, between, constant_throughput
import random


class StressTestUser(HttpUser):
    """
    Aggressive user for stress testing
    """
    
    # Shorter wait time = more aggressive
    wait_time = between(0.5, 1)
    
    
    @task(10)
    def rapid_fire_requests(self):
        """
        Send multiple requests in quick succession
        Simulates heavy load
        """
        endpoints = ["/posts", "/users", "/comments", "/albums"]
        
        for endpoint in endpoints:
            self.client.get(endpoint)
    
    
    @task(5)
    def concurrent_writes(self):
        """
        Test write operations under stress
        """
        post_data = {
            "title": f"Stress Test {random.randint(1, 10000)}",
            "body": "Testing system under stress",
            "userId": random.randint(1, 100)
        }
        
        self.client.post("/posts", json=post_data)


class NormalUser(HttpUser):
    """
    Normal user with regular behavior
    Mix this with StressTestUser to simulate mixed load
    """
    
    wait_time = between(2, 5)
    
    
    @task
    def browse_posts(self):
        """
        Normal browsing behavior
        """
        self.client.get("/posts")
        
        # Read a random post
        post_id = random.randint(1, 100)
        self.client.get(f"/posts/{post_id}")


# Run command:
# locust -f stress_test.py --host=https://jsonplaceholder.typicode.com
# 
# Recommended settings:
# - Users: 500-1000
# - Spawn rate: 50 (aggressive ramp-up)
# - Run until system shows signs of stress
