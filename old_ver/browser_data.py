from playwright.sync_api import sync_playwright, TimeoutError
import pandas as pd
import numpy as np
import datetime


class ParserAviator():
    def __init__(self):
        self.data_current = None
        self.page = None

    def run(self):
        """Запуск и вывод str для дальнейшей обработки"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, timeout=15000)
            self.page = browser.new_page()
            self.page.goto("https://lucky-jet.gamedev-atech.cc/"
                           "?exitUrl=https%253A%252F%252F1wowei.xyz%252Fcasino&language=ru&b=demo")
            try:
                self.page.wait_for_selector(".sc-kAkpmW").click()  # Для клика по кнопке используем див класс находящийся во flex
            except TimeoutError:
                with sync_playwright() as p:
                    browser = p.chromium.launch(headless=True)
                    self.page = browser.new_page()
                    self.page.goto("https://lucky-jet.gamedev-atech.cc/"
                                   "?exitUrl=https%253A%252F%252F1wowei.xyz%252Fcasino&language=ru&b=demo")
                    self.page.wait_for_selector(".sc-kAkpmW").click()
            finally:
                self.page.screenshot(path="../example.png")
                result = self.page.locator(".sc-ggpjZQ").text_content()  # Для замены используем <div id="history" # class="sc-UpCWa fohmDx">
                browser.close()
                return result

    def corr_text_array(self):
        """Текст для array"""
        massive = pd.Series([float(i.replace('\xa0', '')) for i in self.run().split(sep='x') if i != ''])
        while len(massive) != 20:
            massive1 = pd.Series([float(i.replace('\xa0', '')) for i in self.run().split(sep='x') if i != ''])
            return massive1
        return massive

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