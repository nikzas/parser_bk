from current_proj.func_data import ParserAviator
from playwright.sync_api import sync_playwright
import pandas as pd
#Timeout надо исправить


if __name__ == "__main__":
    st = ParserAviator()
    data_current_name = st.get_data()
    ALL_MASSIVE = pd.Series()
    # a1 = st.run()
    # write_to_text = st.correctly_array(a1)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, timeout=15000)
        page = browser.new_page()
        page.goto("https://lucky-jet.gamedev-atech.cc/"
                       "?exitUrl=https%253A%252F%252F1wowei.xyz%252Fcasino&language=ru&b=demo")
        page.wait_for_selector(".sc-kAkpmW").click()
        while True:
            page.screenshot(path="example.png")
            result = page.locator(".sc-ggpjZQ").text_content()
            massive = st.correctly_array(result)
            find_index = massive[:st.found_index(massive[:5], massive)[0]]
            ALL_MASSIVE = pd.concat([find_index, ALL_MASSIVE], ignore_index=True)
            count = massive[:5]
            output_csv = st.save_in_csv(ALL_MASSIVE, data_current_name)

