

from playwright.sync_api import Playwright, sync_playwright, expect

class Parser_Aviator():
    #def __init__(self):

    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            self.page = browser.new_page()
            self.page.goto("https://lucky-jet-ws.1play.one/?exitUrl=null&language=ru&b=demo")
            self.page.locator(".sc-jIILKH > .sc-gYbzsP > .sc-hhOBVt").click()
            self.page.screenshot(path="example.png")
            self.locators = ".sc-dwnOUR"        #Для замены возможного div class
            return self.page.locator(self.locators).text_content()

    def corr_text(self):
        massive = [float(i.replace('\xa0', '')) for i in self.run().split(sep='x') if i != '']
        if len(massive) == 20:
            with open('result', mode='a') as r:
                print(massive, file=r)


if __name__ == "__main__":
    while True:
        start = Parser_Aviator()
        start.corr_text()


