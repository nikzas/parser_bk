from playwright.sync_api import sync_playwright, TimeoutError
import pandas as pd
import numpy as np
import datetime


class ParserAviator():
    def __init__(self):
        self.page = None

    def get_data(self):
        """Запрос времени"""
        return datetime.date.today().isoformat()

    def save_in_csv(self, array_data, data_current):
        """Создание csv"""
        return array_data.to_csv(f'result_to_{data_current}.csv')

    def found_index(self, first_cnt, st_ms):
        window_size = len(first_cnt)
        is_subset = False
        found_indices = []

        for i in range(len(st_ms) - window_size + 1):
            window = st_ms[i:i + window_size]
            if np.array_equal(window, first_cnt):
                is_subset = True
                found_indices = pd.Index(list(range(i, i + window_size)))
                break
        return found_indices

    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, timeout=15000)
            self.page = browser.new_page()
            self.page.goto("https://lucky-jet.gamedev-atech.cc/"
                           "?exitUrl=https%253A%252F%252F1wowei.xyz%252Fcasino&language=ru&b=demo")
            self.page.wait_for_selector(".sc-kAkpmW").click()
            self.page.screenshot(path="example.png")
            result = self.page.locator(".sc-ggpjZQ").text_content()
            return result

    def correctly_array(self, results):
            massive = pd.Series([float(i.replace('\xa0', '')) for i in results.split(sep='x') if i != ''])
            count = massive[:5]
            return count

