from playwright.sync_api import Page, expect, sync_playwright

def playwright_test():
    with sync_playwright() as p:
        # code goes here

playwright_test()