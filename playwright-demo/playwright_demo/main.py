from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Channel can be "chrome", "msedge", "chrome-beta", "msedge-beta" or "msedge-dev".
    browser = p.chromium.launch(channel="chrome", headless=False)
    page = browser.new_page()
    # page.goto("http://playwright.dev")
    page.goto("https://www.whatsmybrowser.org/")

    page.get_by_role("h2", name="Sign in").click()

    print(page.title())

    while True:
        page.wait_for_timeout(10000)

    # browser.close()