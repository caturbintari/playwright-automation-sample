import time
from playwright.sync_api import Playwright

def test_response_time(playwright: Playwright):
    # Setup
    api_context = playwright.request.new_context(
        base_url="https://reqres.in",
        extra_http_headers={
            "Authorization": "Bearer pro_45283557361f02ed70afe9bd225bbc7f6c75fef96a1f488c"
        }
    )
    
    # Start Timer
    start_time = time.perf_counter()
    
    # Request
    response = api_context.get("/api/users?page=2")
    
    # Stop Timer
    end_time = time.perf_counter()
    duration_ms = (end_time - start_time) * 1000
    
    # Assertion (Diset ke 2000ms untuk stabilitas test, Postman default 200ms sering flaky di script)
    assert duration_ms < 2000, f"Response too slow: {duration_ms:.2f}ms"
    
    api_context.dispose()