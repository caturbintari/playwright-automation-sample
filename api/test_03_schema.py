import re
from playwright.sync_api import Playwright

def test_schema_structure(playwright: Playwright):
    # Setup
    api_context = playwright.request.new_context(
        base_url="https://reqres.in",
        extra_http_headers={
            "Authorization": "Bearer pro_45283557361f02ed70afe9bd225bbc7f6c75fef96a1f488c"
        }
    )

    response = api_context.get("/api/users?page=2")
    json_data = response.json()
    
    # Root check
    assert isinstance(json_data, dict)
    expected_root_keys = {'page', 'per_page', 'total', 'total_pages', 'data', 'support'}
    assert expected_root_keys.issubset(json_data.keys()), f"Missing root keys. Got: {json_data.keys()}"

    # 2. Data array check
    assert isinstance(json_data['data'], list)
    email_pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    
    for item in json_data['data']:
        item_keys = {'id', 'email', 'first_name', 'last_name', 'avatar'}
        assert item_keys.issubset(item.keys())
        
        # Type check
        assert isinstance(item['id'], int)
        assert isinstance(item['email'], str)
        assert isinstance(item['first_name'], str)
        assert isinstance(item['last_name'], str)
        assert isinstance(item['avatar'], str)
        assert email_pattern.match(item['email'])

    # Schema check
    assert isinstance(json_data['support'], dict)
    assert {'url', 'text'}.issubset(json_data['support'].keys())

    # Meta section (jika ada)
    if '_meta' in json_data:
        assert isinstance(json_data['_meta'], dict)
        meta_keys = {'powered_by', 'upgrade_url', 'docs_url', 'template_gallery', 'message', 'features', 'upgrade_cta'}
        assert meta_keys.issubset(json_data['_meta'].keys())

    api_context.dispose()