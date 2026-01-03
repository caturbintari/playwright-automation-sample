from playwright.sync_api import Playwright

def test_data_array_content(playwright: Playwright):
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
    assert isinstance(json_data, dict)
    assert isinstance(json_data['data'], list)
    assert len(json_data['data']) > 0, "Data array is empty"

    required_keys = {'id', 'email', 'first_name', 'last_name', 'avatar'}

    for user in json_data['data']:
        assert isinstance(user, dict)
        # Pastikan setiap user memiliki semua key yang dibutuhkan
        assert required_keys.issubset(user.keys()), f"User missing keys: {user}"
        
    api_context.dispose()