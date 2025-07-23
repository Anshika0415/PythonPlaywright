import time

from playwright.sync_api import Page
# def test_playwrightBasics(playwright):
#     print("Testing playwrightBasics")
#     browser=playwright.chromium.launch(headless=False)
#     context=browser.new_context()
#     page=context.new_page()
#     page.goto("https://rahulshettyacademy.com")


#default settings in this page fixtures chromium headless
#page:Page fixture provides auto suggestions
def test_playwrightBasics_1(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    #should have label tag and input tag should be wrapped btw label tag
    #there r three things 1-label 2-input->locator 3-role
    # page.get_by_label("Username:").fill("rahulshettyacademy")
    page.locator("#username").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("stud")
    page.locator("#terms").check()
    page.get_by_role("button").click()
    time.sleep(5)