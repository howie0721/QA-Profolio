"""
Advanced Load Test - Step Load Pattern

This test gradually increases load to find the breaking point.

Test Pattern:
- Start with 10 users
- Every 30 seconds, add 10 more users
- Continue until system breaks or reaches 200 users

This helps identify:
- System capacity
- Performance degradation point
- Resource bottlenecks
"""

from locust import HttpUser, task, between, events
import time


class StepLoadUser(HttpUser):
    """
    User class for step load testing
    """
    
    wait_time = between(1, 2)
    
    
    @task
    def get_posts(self):
        """
        Simple GET request to posts endpoint
        """
        response = self.client.get("/posts")
        
        # Log slow responses
        if response.elapsed.total_seconds() > 1.0:
            print(f"⚠️ Slow response: {response.elapsed.total_seconds():.2f}s")


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """
    Called when test starts
    """
    print("🚀 Performance test starting...")
    print(f"Target: {environment.host}")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    """
    Called when test stops
    Print summary statistics
    """
    print("\n" + "="*50)
    print("📊 Test Summary")
    print("="*50)
    
    stats = environment.stats
    
    print(f"Total requests: {stats.total.num_requests}")
    print(f"Total failures: {stats.total.num_failures}")
    print(f"Success rate: {((stats.total.num_requests - stats.total.num_failures) / stats.total.num_requests * 100):.2f}%")
    print(f"Average response time: {stats.total.avg_response_time:.2f}ms")
    print(f"Max response time: {stats.total.max_response_time:.2f}ms")
    print(f"RPS: {stats.total.current_rps:.2f}")
    print("="*50)


# To run this test with step load:
# locust -f step_load_test.py --host=https://jsonplaceholder.typicode.com --users 200 --spawn-rate 10 --run-time 5m
