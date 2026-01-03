from playwright.sync_api import Playwright, sync_playwright

# Scenario: Test API GET request
def test_get(playwright: Playwright):
    # requext context setup
    api_context = playwright.request.new_context(
        base_url="https://reqres.in" # Opsional: Set base URL agar lebih rapi
    )
    
    # request dengan header Authorization
    response = api_context.get("/api/users?page=2", headers={
        "Authorization": "Bearer pro_45283557361f02ed70afe9bd225bbc7f6c75fef96a1f488c"
    })
    
    # validasi
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    
    # cleanup
    api_context.dispose()