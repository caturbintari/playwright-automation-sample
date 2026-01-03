from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com/"
USER = "standard_user"
PASS = "secret_sauce"

def login_to_app(page: Page):
    page.goto(URL)
    page.locator("[data-test='username']").fill(USER)
    page.locator("[data-test='password']").fill(PASS)
    page.locator("[data-test='login-button']").click()

# 1. user login 
def test_login_basic(page: Page):
    login_to_app(page)
    
    # Validasi: URL harus berubah ke halaman inventory
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

# 2. login with enter keybaord action
def test_login_enter_key(page: Page):
    page.goto(URL)
    page.locator("[data-test='username']").fill(USER)
    page.locator("[data-test='password']").fill(PASS)

    page.locator("[data-test='password']").press("Enter")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

# 3. invetory list loaded
def test_inventory_list_loaded(page: Page):
    login_to_app(page)
    expect(page.locator(".inventory_item")).not_to_have_count(0)

# 4. default sorting (A to Z)
def test_default_sorting(page: Page):
    login_to_app(page)
    expect(page.locator(".active_option")).to_have_text("Name (A to Z)")

# 5. session persistence after reload
def test_session_persistence(page: Page):
    login_to_app(page)
    page.reload()

    expect(page.locator(".shopping_cart_link")).to_be_visible()