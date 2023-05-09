from playwright.sync_api import Page, expect, sync_playwright

# playwright 
def playwright_test():
    with sync_playwright() as p:
        # launch chromiom with new tab
        browser = p.chromium.launch(headless=False) # headless defines if the browser will be opened for debugging or not
        page = browser.new_page()
        page.goto("https://google.com")
        # get an image from the HTML document
        img_src = page.query_selector("img").get_attribute("src")
        print(img_src)
        # close the browser
        browser.close()

playwright_test()