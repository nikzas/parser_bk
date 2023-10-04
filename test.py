from playwright.sync_api import Playwright, sync_playwright, expect


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://lucky-jet-ws.1play.one/?exitUrl=null&language=ru&b=demo")
        page.locator(".sc-jIILKH > .sc-gYbzsP > .sc-hhOBVt").click()
        page.screenshot(path="example.png")
        locators = ".sc-dwnOUR"
        return page.locator(locators).text_content()


def corr_text():
    massive = [float(i) for i in run().split(sep='x') if i != '']
    if len(massive) == 20:
        with open('result', mode='a') as r:
            print(massive, file=r)


while True:
    corr_text()

