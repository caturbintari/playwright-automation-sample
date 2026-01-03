import re
from playwright.sync_api import Playwright

def test_support_url_format(playwright: Playwright):
    # Setup
    api_context = playwright.request.new_context(
        base_url="https://reqres.in",
        extra_http_headers={
            "Authorization": "Bearer pro_45283557361f02ed70afe9bd225bbc7f6c75fef96a1f488c"
        }
    )
    
    response = api_context.get("/api/users?page=2")
    json_data = response.json()
    
    # Assertion
    support_data = json_data.get('support', {})
    support_url = support_data.get('url')
    
    assert isinstance(support_url, str), "Support URL is not a string"
    
    # Regex untuk validasi URL (http/https/ftp)
    url_pattern = re.compile(r"^(https?|ftp)://[^\s/$.?#].[^\s]*$")
    
    assert url_pattern.match(support_url), f"URL format is invalid: {support_url}"
    
    api_context.dispose()