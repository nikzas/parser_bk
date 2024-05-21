from playwright.sync_api import sync_playwright


def get_new_numbers():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, timeout=15000)
        page = browser.new_page()
        page.goto("https://lucky-jet.gamedev-atech.cc/"
                  "?exitUrl=https%253A%252F%252F1wowei.xyz%252Fcasino&language=ru&b=demo")
        page.wait_for_selector(".sc-kAkpmW").click()
        while True:
            page.screenshot(path="example.png")
            result = page.locator(".sc-ggpjZQ").text_content()
            print(result)

# Запуск функции для получения новых чисел в бесконечном цикле
while True:
    get_new_numbers()
