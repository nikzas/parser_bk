from playwright.sync_api import sync_playwright
from current_proj.func_data import ParserAviator
import pandas as pd


st = ParserAviator()
data_current_name = st.get_data()

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, timeout=15000)
        page = browser.new_page()
        page.goto("https://lucky-jet.gamedev-atech.cc/"
                       "?exitUrl=https%253A%252F%252F1wowei.xyz%252Fcasino&language=ru&b=demo")
        page.wait_for_selector(".sc-kAkpmW").click()
        page.screenshot(path="example.png")
        result = page.locator(".sc-ggpjZQ").text_content()
        return result

        text = st.correctly_array(result)

        while True:
            page.screenshot(path="example.png")
            result = page.locator(".sc-ggpjZQ").text_content()
            massive = pd.Series([float(i.replace('\xa0', '')) for i in result.split(sep='x') if i != ''])
            """----------------------------------Запуск 2 массива----------------------------------"""

            find_index = massive[:st.found_index(count, massive)[0]]
            ALL_MASSIVE = pd.concat([find_index, ALL_MASSIVE], ignore_index=True)
            count = massive[:5]
            output_csv = st.save_in_csv(ALL_MASSIVE, data_current_name)
            print(f"Next 'while' {ALL_MASSIVE}")
