import pytest
from playwright.sync_api import Page, expect

# 1. wrong password
def test_login_wrong_password(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("caturbintari") # wrong password
    page.locator("[data-test='login-button']").click()
    
    # error message validation
    error_msg = page.locator("[data-test='error']")
    expect(error_msg).to_be_visible()
    expect(error_msg).to_contain_text("Username and password do not match")

# 2. wrong username
def test_login_wrong_username(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test='username']").fill("caturbintari") # wrong username
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    
    error_msg = page.locator("[data-test='error']")
    expect(error_msg).to_be_visible()
    expect(error_msg).to_contain_text("Username and password do not match")

# 3. empty username
def test_login_empty_username(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    
    error_msg = page.locator("[data-test='error']")
    expect(error_msg).to_be_visible()
    expect(error_msg).to_have_text("Epic sadface: Username is required")

# 4. empty password
def test_login_empty_password(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='login-button']").click()
    
    error_msg = page.locator("[data-test='error']")
    expect(error_msg).to_be_visible()
    expect(error_msg).to_have_text("Epic sadface: Password is required")

# 5. locked out user
def test_login_locked_out_user(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test='username']").fill("locked_out_user") 
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    
    error_msg = page.locator("[data-test='error']")
    expect(error_msg).to_be_visible()
    expect(error_msg).to_contain_text("Sorry, this user has been locked out")