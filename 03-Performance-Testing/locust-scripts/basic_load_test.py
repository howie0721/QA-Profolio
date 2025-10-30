"""
Basic Load Test - JSONPlaceholder API

This is a simple load test that simulates users making API requests.

Test Target: https://jsonplaceholder.typicode.com
- A free fake REST API for testing and prototyping

What this test does:
- Simulates multiple users accessing the API
- Tests GET requests for posts
- Measures response time and success rate
"""

from locust import HttpUser, task, between
import random


class APIUser(HttpUser):
    """
    Represents a user making API requests
    
    Each instance of this class is a virtual user
    """
    
    # Wait time between tasks (1-3 seconds)
    # This makes it more realistic - users don't click instantly
    wait_time = between(1, 3)
    
    # Base URL - will be set when starting Locust
    # You can also hardcode it: host = "https://jsonplaceholder.typicode.com"
    
    
    def on_start(self):
        """
        Called when a user starts
        Use this for login or initial setup
        """
        print("A new user has started!")
    
    
    @task(5)  # Weight 5 - this task runs 5 times more often than others
    def get_all_posts(self):
        """
        Task: Get all posts
        This is the most common operation (weight 5)
        """
        with self.client.get("/posts", catch_response=True) as response:
            if response.status_code == 200:
                # Success!
                response.success()
            else:
                # Mark as failure
                response.failure(f"Got status code {response.status_code}")
    
    
    @task(3)  # Weight 3
    def get_single_post(self):
        """
        Task: Get a single post by ID
        Randomly selects a post ID between 1-100
        """
        post_id = random.randint(1, 100)
        
        with self.client.get(f"/posts/{post_id}", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")
    
    
    @task(2)  # Weight 2
    def get_post_comments(self):
        """
        Task: Get comments for a post
        This operation is less common (weight 2)
        """
        post_id = random.randint(1, 100)
        
        with self.client.get(f"/posts/{post_id}/comments", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")
    
    
    @task(1)  # Weight 1
    def get_users(self):
        """
        Task: Get all users
        This is the least common operation (weight 1)
        """
        with self.client.get("/users", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")
    
    
    @task(1)
    def create_post(self):
        """
        Task: Create a new post (POST request)
        Tests write operations
        """
        post_data = {
            "title": "Performance Test Post",
            "body": "This is a test post created during load testing",
            "userId": random.randint(1, 10)
        }
        
        with self.client.post("/posts", json=post_data, catch_response=True) as response:
            if response.status_code == 201:  # 201 = Created
                response.success()
            else:
                response.failure(f"Expected 201 but got {response.status_code}")


# To run this test:
# 1. Save this file
# 2. Run: locust -f basic_load_test.py
# 3. Open browser: http://localhost:8089
# 4. Enter:
#    - Number of users: 100
#    - Spawn rate: 10
#    - Host: https://jsonplaceholder.typicode.com
# 5. Click "Start swarming"
