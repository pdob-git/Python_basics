import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("link", name="How to install Playwright").click()
    page.get_by_text("init playwright@latest").click(button="right")
    page.get_by_text("Run the install command and").click(button="right")
    page.get_by_text("Playwright will download the").click(button="right")
    page.get_by_text("Run the install command and").click()
    page.get_by_role("main").locator("div").filter(has_text="Getting StartedInstallationOn").nth(2).click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
